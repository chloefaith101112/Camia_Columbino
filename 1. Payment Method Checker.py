 # Chloe Faith Columbino
 # 8-Camia
 # Payment Method Checker

valid_payment_method = ["gcash", "cash", "card"]

payment_method = input("Please enter your payment method: ").lower()

if payment_method in valid_payment_method:
    print("Valid payment method")
else :
    print("Invalid payment method")