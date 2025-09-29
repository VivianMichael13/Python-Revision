# Find the sum of digits of a given number.

n = int(input("Enter a number: "))
x=n
sum = 0

while n>0:
    sum += n%10
    n//=10
    
print(f"Sum of digits of {x} is: {sum}")