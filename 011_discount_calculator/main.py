price = float(input("Enter the product price (R$): "))
discount_percent = float(input("Enter the discount percentage (%): "))

discount_amount = (discount_percent / 100) * price
final_price = price - discount_amount

print(f"\nOriginal price: R${price:.2f}")
print(f"Discount: {discount_percent:.1f}% (R${discount_amount:.2f})")
print(f"Final price after discount: R${final_price:.2f}")