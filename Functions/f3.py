def greater(a,b):
    if a > b:
        print(a,"is greater than",b)
    elif a < b:
        print(b,"is greater than",a)
    else:
        print(a,"is equal to",b)

a = int(input("Enter first number: "))
b = int(input("Enter second number: "))
greater(a,b)