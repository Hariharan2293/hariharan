from math import factorial

rows = int(input("Enter the number of rows: "))

for i in range(0, rows):
    for j in range(rows - i + 1):
        print(end = ' ')
    for k in range(0, i + 1):
        print(factorial(i)//(factorial(k) * factorial(i - k)), end = ' ')
    print()

