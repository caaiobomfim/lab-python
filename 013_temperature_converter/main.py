celsius = float(input("Enter the temperature in Celsius (°C): "))

fahrenheit = (celsius * 9/5) + 32
kelvin = celsius + 273.15

print(f"\nTemperature in Celsius: {celsius:.2f}°C")
print(f"In Fahrenheit: {fahrenheit:.2f}°F")
print(f"In Kelvin: {kelvin:.2f}K")