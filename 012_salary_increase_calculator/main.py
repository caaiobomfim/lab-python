salary = float(input("Enter the current salary (R$): "))
increase_percent = float(input("Enter the percentage of salary increase (%): "))

increase_amount = (increase_percent / 100) * salary
new_salary = salary + increase_amount

print(f"\nOriginal salary: R${salary:.2f}")
print(f"Increase: {increase_percent:.1f}% (R${increase_amount:.2f})")
print(f"New salary after increase: R${new_salary:.2f}")