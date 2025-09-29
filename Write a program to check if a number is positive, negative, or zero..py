# Write a program to check if a number is positive, negative, or zero.

n = int(input("Enter a number: "))

if n>0:
    print(f"{n} is positive.")
elif n<0:
    print(f"{n} is negative.")
else:
    print("Zero.")