def total_bill(prices, quantities):
    total = 0

    for i in range(len(prices)):
        total += prices[i] * quantities[i]

    discount = total * 0.10
    final_bill = total - discount

    return final_bill


prices = list(map(float, input("Enter prices: ").split()))
quantities = list(map(int, input("Enter quantities: ").split()))
print("Final bill after 10% Discount:", total_bill(prices, quantities))