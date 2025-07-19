reais = float(input("Enter an amount in BRL (R$): "))
exchange_rate = float(input("Enter the current USD exchange rate (e.g., 5.20): "))

dollars = reais / exchange_rate

print(f"With R${reais:.2f}, you can buy ${dollars:.2f} USD at an exchange rate of {exchange_rate:.2f}")