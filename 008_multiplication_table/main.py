number = int(input("Enter a number to see its multiplication table: "))

print(f"\nMultiplication table of {number}:\n")

for i in range(1, 11):
    result = number * i
    print(f"{number} x {i:2} = {result}")