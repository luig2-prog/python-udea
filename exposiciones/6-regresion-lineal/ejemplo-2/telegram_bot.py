import os
import logging
import json
from datetime import datetime
from telegram import Update, InlineKeyboardButton, InlineKeyboardMarkup
from telegram.ext import Application, CommandHandler, MessageHandler, filters, ContextTypes, ConversationHandler, CallbackQueryHandler
import pandas as pd
import numpy as np
from sklearn.linear_model import LinearRegression
import joblib

# Enable logging
logging.basicConfig(
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
    level=logging.INFO
)
logger = logging.getLogger(__name__)

# Estados de la conversación
PESO, CILINDRADA, TIPO_MOTOR = range(3)

# Archivo para guardar predicciones
PREDICCIONES_FILE = "predicciones.json"

# Ejemplos de vehículos
EJEMPLOS_VEHICULOS = {
    "Sedan": {"peso": 1200, "cilindrada": 1600, "tipo": "Gasolina"},
    "SUV": {"peso": 1800, "cilindrada": 2000, "tipo": "Diésel"},
    "Deportivo": {"peso": 1500, "cilindrada": 3000, "tipo": "Gasolina"},
    "Compacto": {"peso": 1000, "cilindrada": 1200, "tipo": "Gasolina"}
}

# Saludos reconocidos
SALUDOS = ['hola', 'buenas', 'buenos dias', 'buenas tardes', 'buenas noches', 'saludos', 'hey', 'hi', 'hello']

# Cargar el modelo
def cargar_modelo():
    file_path = os.path.join(os.path.dirname(__file__), "datos_consumo.xlsx")
    df = pd.read_excel(file_path)
    df['Tipo Motor'] = df['Tipo Motor'].map({'Gasolina': 0, 'Diésel': 1})
    
    X = df[['Peso (kg)', 'Cilindrada (cc)', 'Tipo Motor']]
    y = df['Consumo (L/100km)']
    
    modelo = LinearRegression()
    modelo.fit(X, y)
    return modelo, df

# Función para predecir consumo
def predecir_consumo(modelo, peso, cilindrada, tipo_motor):
    datos = pd.DataFrame({
        'Peso (kg)': [peso],
        'Cilindrada (cc)': [cilindrada],
        'Tipo Motor': [tipo_motor]
    })
    return modelo.predict(datos)[0]

# Guardar predicción
def guardar_prediccion(usuario_id, prediccion):
    if not os.path.exists(PREDICCIONES_FILE):
        predicciones = {}
    else:
        try:
            with open(PREDICCIONES_FILE, 'r') as f:
                predicciones = json.load(f)
        except:
            predicciones = {}
    
    if str(usuario_id) not in predicciones:
        predicciones[str(usuario_id)] = []
    
    predicciones[str(usuario_id)].append({
        "fecha": datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
        "datos": prediccion
    })
    
    with open(PREDICCIONES_FILE, 'w') as f:
        json.dump(predicciones, f, indent=4)

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE) -> int:
    await update.message.reply_text(
        "¡Bienvenido al bot de predicción de consumo de combustible! 🚗\n\n"
        "Voy a ayudarte a predecir el consumo de combustible de tu vehículo.\n"
        "Por favor, ingresa el peso del vehículo en kilogramos:"
    )
    return PESO

async def help_command(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    help_text = """
🤖 *Comandos disponibles:*

/start - Iniciar una nueva predicción
/help - Mostrar esta ayuda
/stats - Ver estadísticas del modelo
/ejemplos - Ver ejemplos de vehículos
/historial - Ver tu historial de predicciones
/cancel - Cancelar la operación actual

*Instrucciones:*
1. Usa /start para comenzar una predicción
2. Sigue las instrucciones del bot
3. Ingresa los datos solicitados
4. Recibe tu predicción de consumo

*Notas:*
- El peso debe estar en kilogramos
- La cilindrada debe estar en centímetros cúbicos (cc)
- El tipo de motor puede ser Gasolina o Diésel
"""
    await update.message.reply_text(help_text, parse_mode='Markdown')

async def stats_command(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    try:
        modelo, df = cargar_modelo()
        stats = df.describe()
        
        mensaje = "📊 *Estadísticas del Modelo:*\n\n"
        mensaje += f"*Rango de pesos:* {stats['Peso (kg)']['min']:.1f} - {stats['Peso (kg)']['max']:.1f} kg\n"
        mensaje += f"*Rango de cilindradas:* {stats['Cilindrada (cc)']['min']:.1f} - {stats['Cilindrada (cc)']['max']:.1f} cc\n"
        mensaje += f"*Rango de consumo:* {stats['Consumo (L/100km)']['min']:.1f} - {stats['Consumo (L/100km)']['max']:.1f} L/100km\n\n"
        mensaje += f"*Coeficientes del modelo:*\n"
        for feature, coef in zip(['Peso', 'Cilindrada', 'Tipo Motor'], modelo.coef_):
            mensaje += f"- {feature}: {coef:.6f}\n"
        mensaje += f"*Intercepto:* {modelo.intercept_:.6f}"
        
        await update.message.reply_text(mensaje, parse_mode='Markdown')
    except Exception as e:
        await update.message.reply_text(f"❌ Error al obtener estadísticas: {str(e)}")

async def ejemplos_command(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    keyboard = []
    for tipo, datos in EJEMPLOS_VEHICULOS.items():
        keyboard.append([InlineKeyboardButton(tipo, callback_data=tipo)])
    
    reply_markup = InlineKeyboardMarkup(keyboard)
    await update.message.reply_text(
        "Selecciona un tipo de vehículo para ver sus características:",
        reply_markup=reply_markup
    )

async def button_callback(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    query = update.callback_query
    await query.answer()
    
    tipo = query.data
    datos = EJEMPLOS_VEHICULOS[tipo]
    
    mensaje = f"🚗 *{tipo}*\n\n"
    mensaje += f"Peso: {datos['peso']} kg\n"
    mensaje += f"Cilindrada: {datos['cilindrada']} cc\n"
    mensaje += f"Tipo de motor: {datos['tipo']}\n\n"
    mensaje += "Usa /start para predecir el consumo de este vehículo"
    
    await query.edit_message_text(text=mensaje, parse_mode='Markdown')

async def historial_command(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    try:
        if not os.path.exists(PREDICCIONES_FILE):
            await update.message.reply_text("No hay predicciones guardadas.")
            return
        
        with open(PREDICCIONES_FILE, 'r') as f:
            predicciones = json.load(f)
        
        usuario_id = str(update.effective_user.id)
        if usuario_id not in predicciones or not predicciones[usuario_id]:
            await update.message.reply_text("No tienes predicciones guardadas.")
            return
        
        mensaje = "📋 *Tu historial de predicciones:*\n\n"
        for pred in predicciones[usuario_id][-5:]:  # Mostrar las últimas 5 predicciones
            mensaje += f"*Fecha:* {pred['fecha']}\n"
            mensaje += f"Peso: {pred['datos']['peso']} kg\n"
            mensaje += f"Cilindrada: {pred['datos']['cilindrada']} cc\n"
            mensaje += f"Tipo de motor: {pred['datos']['tipo_motor']}\n"
            mensaje += f"Consumo estimado: {pred['datos']['consumo']:.1f} L/100km\n\n"
        
        await update.message.reply_text(mensaje, parse_mode='Markdown')
    except Exception as e:
        await update.message.reply_text(f"❌ Error al obtener el historial: {str(e)}")

async def peso(update: Update, context: ContextTypes.DEFAULT_TYPE) -> int:
    try:
        peso = float(update.message.text)
        if peso <= 0:
            await update.message.reply_text("❌ El peso debe ser mayor que 0.")
            return PESO
        if peso > 5000:
            await update.message.reply_text("⚠️ El peso parece muy alto. ¿Estás seguro?")
            return PESO
        
        context.user_data['peso'] = peso
        await update.message.reply_text(
            "¡Perfecto! Ahora ingresa la cilindrada del motor en centímetros cúbicos (cc):"
        )
        return CILINDRADA
    except ValueError:
        await update.message.reply_text(
            "❌ Por favor, ingresa un número válido para el peso."
        )
        return PESO

async def cilindrada(update: Update, context: ContextTypes.DEFAULT_TYPE) -> int:
    try:
        cilindrada = float(update.message.text)
        if cilindrada <= 0:
            await update.message.reply_text("❌ La cilindrada debe ser mayor que 0.")
            return CILINDRADA
        if cilindrada > 10000:
            await update.message.reply_text("⚠️ La cilindrada parece muy alta. ¿Estás seguro?")
            return CILINDRADA
        
        context.user_data['cilindrada'] = cilindrada
        await update.message.reply_text(
            "¡Excelente! Ahora indica el tipo de motor (Gasolina/Diésel):"
        )
        return TIPO_MOTOR
    except ValueError:
        await update.message.reply_text(
            "❌ Por favor, ingresa un número válido para la cilindrada."
        )
        return CILINDRADA

async def tipo_motor(update: Update, context: ContextTypes.DEFAULT_TYPE) -> int:
    tipo_motor = update.message.text.lower()
    if tipo_motor.startswith('d'):
        tipo_motor_valor = 1
        tipo_motor_nombre = "Diésel"
    else:
        tipo_motor_valor = 0
        tipo_motor_nombre = "Gasolina"
    
    context.user_data['tipo_motor'] = tipo_motor_valor
    
    try:
        # Realizar la predicción
        modelo, _ = cargar_modelo()
        consumo = predecir_consumo(
            modelo,
            context.user_data['peso'],
            context.user_data['cilindrada'],
            tipo_motor_valor
        )
        
        # Guardar la predicción
        prediccion = {
            'peso': context.user_data['peso'],
            'cilindrada': context.user_data['cilindrada'],
            'tipo_motor': tipo_motor_nombre,
            'consumo': float(consumo)
        }
        guardar_prediccion(update.effective_user.id, prediccion)
        
        await update.message.reply_text(
            f"📊 *Resultados de la predicción:*\n\n"
            f"Peso: {context.user_data['peso']} kg\n"
            f"Cilindrada: {context.user_data['cilindrada']} cc\n"
            f"Tipo de motor: {tipo_motor_nombre}\n\n"
            f"Consumo estimado: {consumo:.1f} L/100km\n\n"
            f"Usa /historial para ver tus predicciones guardadas",
            parse_mode='Markdown'
        )
        
        return ConversationHandler.END
    except Exception as e:
        await update.message.reply_text(f"❌ Error al realizar la predicción: {str(e)}")
        return ConversationHandler.END

async def cancel(update: Update, context: ContextTypes.DEFAULT_TYPE) -> int:
    await update.message.reply_text(
        "Operación cancelada. Usa /start para comenzar de nuevo."
    )
    return ConversationHandler.END

async def handle_greeting(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    """Maneja los mensajes de saludo y muestra el menú de opciones."""
    mensaje = update.message.text.lower()
    if mensaje in SALUDOS:
        await update.message.reply_text(
            "¡Hola! 👋 Soy tu asistente para predecir el consumo de combustible.\n\n"
            "¿En qué puedo ayudarte? Aquí están mis comandos:\n\n"
            "🚗 /start - Iniciar una nueva predicción\n"
            "📊 /stats - Ver estadísticas del modelo\n"
            "🚘 /ejemplos - Ver ejemplos de vehículos\n"
            "📋 /historial - Ver tu historial de predicciones\n"
            "❓ /help - Ver ayuda detallada\n"
            "❌ /cancel - Cancelar la operación actual\n\n"
            "¡Elige una opción y empecemos! 😊"
        )

def main() -> None:
    # Reemplaza 'TU_TOKEN_AQUI' con el token de tu bot
    application = Application.builder().token('TU_TOKEN_AQUI').build()

    # Manejadores de comandos
    application.add_handler(CommandHandler("help", help_command))
    application.add_handler(CommandHandler("stats", stats_command))
    application.add_handler(CommandHandler("ejemplos", ejemplos_command))
    application.add_handler(CommandHandler("historial", historial_command))
    
    # Manejador de saludos
    application.add_handler(MessageHandler(filters.TEXT & ~filters.COMMAND, handle_greeting))
    
    # Manejador de botones
    application.add_handler(CallbackQueryHandler(button_callback))

    # Manejador de conversación
    conv_handler = ConversationHandler(
        entry_points=[CommandHandler('start', start)],
        states={
            PESO: [MessageHandler(filters.TEXT & ~filters.COMMAND, peso)],
            CILINDRADA: [MessageHandler(filters.TEXT & ~filters.COMMAND, cilindrada)],
            TIPO_MOTOR: [MessageHandler(filters.TEXT & ~filters.COMMAND, tipo_motor)],
        },
        fallbacks=[CommandHandler('cancel', cancel)],
    )

    application.add_handler(conv_handler)
    application.run_polling()

if __name__ == '__main__':
    main() 