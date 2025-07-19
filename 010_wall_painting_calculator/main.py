height = float(input("Enter the height of the wall (in meters): "))
width = float(input("Enter the width of the wall (in meters): "))

area = height * width
paint_needed = area / 2  # 1 liter of paint covers 2 m²

print(f"\nWall dimensions: {height:.2f}m x {width:.2f}m")
print(f"Total area: {area:.2f} square meters")
print(f"Paint required: {paint_needed:.2f} liters")