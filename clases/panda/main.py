import pandas as pd

mydataset = {
    'cars': ["BMW", "Volvo", "Ford"],
    'passings': [3, 7, 2]
}

myvar = pd.DataFrame(mydataset)

print(myvar)

print(pd.__version__)

data = {
    "calories": [420, 380, 390],
    "duration": [50, 40, 45],
    "gramosperdidos": [50, 47, 48]
}

df = pd.DataFrame(data, index = ["day1", "day2", "day3"])

print(df)
print(df.loc["day2"])

"""
Load Files into a DataFrame
"""

print("============== CSV ===============")

dffile = pd.read_csv('data.csv')
dffile2 = pd.read_csv('data-atcome.csv', sep=';')

print(dffile)
print(dffile2)

