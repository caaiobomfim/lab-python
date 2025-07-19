days = int(input("How many days was the car rented? "))
km = float(input("How many kilometers did the car travel? "))

daily_rate = 60.00       # R$ per day
km_rate = 0.15           # R$ per km

total_cost = (days * daily_rate) + (km * km_rate)

print(f"\nRental duration: {days} day(s)")
print(f"Distance traveled: {km:.1f} km")
print(f"Total amount to pay: R${total_cost:.2f}")