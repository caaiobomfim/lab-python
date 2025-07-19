#string
s1 = str(input('Enter the first string: '))
s2 = str(input('Enter the second string: '))
concat = s1 + s2
print('Concatenated string:', concat)
print('Type:', type(concat))

#int
i1 = int(input('Enter the first number: '))
i2 = int(input('Enter the second number: '))
sum1 = i1 + i2
print('Result(int):', sum1)
print('Result(int): {}'.format(sum1))
print('The sum of {} and {} is {}'.format(i1, i2, sum1))
print('Type:', type(sum1))

#float
f1 = float(input('Enter the first number: '))
f2 = float(input('Enter the second number: '))
sum2 = f1 + f2
print('Result(float):', sum2)
print('Result(float): {}'.format(sum2))
print('The sum of {} and {} is {}'.format(f1, f2, sum2))
print('Type:', type(sum2))

#boolean (True/False)
b = bool(input('Enter the boolean: '))
print('Result(boolean):', b)
print('Type:', type(b))

#Methods
m = input('Enter any text: ')
print(m.isnumeric())
print(m.isalpha())
print(m.isalnum())
print(m.isupper())