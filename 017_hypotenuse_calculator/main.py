import math

co = float(input("Enter the length of the opposite side: "))
ca = float(input("Enter the length of the adjacent side: "))

hypotenuse = math.hypot(co, ca)

print(f"The hypotenuse is {hypotenuse:.2f}")