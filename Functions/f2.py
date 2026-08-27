def check_even_odd(n):
    if n % 2 == 0:
        print(n,"is even.")
    else:
        print(n,"is odd.")

n = int(input("Enter a number: "))
check_even_odd(n)