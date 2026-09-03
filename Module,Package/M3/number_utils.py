def prime(n):
    if n < 2:
        return False

    for i in range(2, n):
        if n % i == 0:
            return False
    return True

def palindrome(n):
    return str(n) == str(n)[::-1]

def armstrong(n):
    s = 0
    temp = n
    while temp > 0:
        digit = temp % 10
        s = s + digit ** 3
        temp = temp // 10

    return s == n

def perfect(n):
    s = 0

    for i in range(1, n):
        if n % i == 0:
            s = s + i
    return s == n