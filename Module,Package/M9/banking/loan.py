def loan_amount(principal, rate, time):
    interest = principal * rate * time / 100
    return principal + interest