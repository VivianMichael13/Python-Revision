# Find the largest of three numbers.

a = int(input("Enter first number: "))

b = int(input("Enter second number: "))

c = int(input("Enter third number: "))

if a>b and a>c:
    print(f"{a} is largest.")
elif b>a and b>c:
    print(f"{b} is largest.")
else:
    print(f"{c} is largest.")
