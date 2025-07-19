import math

angle = float(input("Enter the angle in degrees: "))

radians = math.radians(angle)

sine = math.sin(radians)
cosine = math.cos(radians)
tangent = math.tan(radians)

print(f"Sine: {sine:.4f}")
print(f"Cosine: {cosine:.4f}")
print(f"Tangent: {tangent:.4f}")
