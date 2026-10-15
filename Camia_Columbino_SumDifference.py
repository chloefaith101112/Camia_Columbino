
num1 = int(input("Enter the first number: "))
num2 = int(input("Enter the second number: "))
sum = 0
difference = 0


def calculate_sum():
    global sum
    sum = num1 + num2

def calculate_difference():
    global difference
    difference = num1 - num2

calculate_sum()
calculate_difference()

print("Sum:", sum)
print("Difference:", difference)













