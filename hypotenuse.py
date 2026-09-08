#Author: Chloe Faith L. Columbino
#Section: 8-Camia

#Imports the math library
import math

#Asks the user the lengths of the hypotenuse
lengtha=float(input("Enter the number of side a:"))
lengthb=float(input("Enter the number of side b:"))

#Compute the hypotenuse using the pythagorean thorem
a1 = math.pow(lengtha,2)
b1 = math.pow(lengthb,2)
add= a1+b1
c=math.sqrt(add)

#Shows result
print(f"The length of the hypotenuse is: {c:.2f}")