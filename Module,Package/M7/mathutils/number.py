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
    total = 0
    temp = n
    while temp > 0:
        digit = temp % 10
        total = total + digit ** 3
        temp = temp // 10
    return total == n