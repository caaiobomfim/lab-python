meters = float(input("Enter a value in meters: "))

print(f"{meters} meters is equivalent to:")
print(f"- {meters * 1000:.0f} millimeters (mm)")
print(f"- {meters * 100:.0f} centimeters (cm)")
print(f"- {meters * 10:.0f} decimeters (dm)")
print(f"- {meters / 10:.2f} decameters (dam)")
print(f"- {meters / 100:.2f} hectometers (hm)")
print(f"- {meters / 1000:.3f} kilometers (km)")