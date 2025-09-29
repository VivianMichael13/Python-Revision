# Reverse a given string without using slicing.

n = int(input("Enter a number: "))

x=n

reverse = 0

while n>0:
    reverse= reverse*10 + n%10
    n//=10

print(f"reverse of {x} is {reverse}")