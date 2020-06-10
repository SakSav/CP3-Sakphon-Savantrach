number = int(input("Enter a number and you will see a Pyramid : " ))
for i in range(number):
    print(" "*(number-i-1) + "*"*(2*i+1))