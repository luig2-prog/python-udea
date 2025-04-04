has_license = True
knows_how_to_drive = False
can_to_drive = has_license and knows_how_to_drive

print(can_to_drive)

has_vip = True
has_regular = False
can_enter_event = has_vip or has_regular
print(can_enter_event)

not_knows_how_to_drive = not knows_how_to_drive
print(not_knows_how_to_drive)