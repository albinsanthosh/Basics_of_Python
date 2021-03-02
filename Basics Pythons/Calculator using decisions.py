a = int(input('Enter a number'))
b = int(input('Enter second number'))
c = int(input('Enter an Option 1.Add 2.Subtract 3.Multiply 4.Divide'))
if (c == 1):
    print(f'Sum is ', a + b)
elif (c == 2):
    print(f'Difference is ', a - b)
elif (c == 3):
    print(f'Product is ', a * b)
elif (c == 4):
    print(f'Quotient is ', a / b)
else:
    print(f'Invalid Option selected')