def vatCalculator(Price):
    result = Price * 1.07
    return result

print(vatCalculator(int(input("Price : "))))