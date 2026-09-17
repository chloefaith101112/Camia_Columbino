# Chloe Faith Columbino
# 8-Camia
# PIN Validator

pin = input("Create a 6-digit PIN: ")

if len(pin) == 6 and pin.isdigit():
    print("Valid PIN")
else:
    print("Invalid PIN. Enter exactly 6 digits.")