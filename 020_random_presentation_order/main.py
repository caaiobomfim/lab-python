import random

name1 = input("Enter the name of the first person: ")
name2 = input("Enter the name of the second person: ")
name3 = input("Enter the name of the third person: ")
name4 = input("Enter the name of the fourth person: ")

names = [name1, name2, name3, name4]
random.shuffle(names)

print("The presentation order will be:")
for index, name in enumerate(names, start=1):
    print(f"{index}. {name}")