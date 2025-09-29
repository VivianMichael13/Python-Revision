# Check if a number is an Armstrong number.

n = int(input("Enter a number: "))
digc = 0
tempn=n
x=n
sum = 0

while tempn>0:
    digc+=1
    tempn//=10

while n>0:
    dig = n%10
    sum += dig**digc
    n//=10

if sum == x:
    print(f"{x} is an armstrong number.")
else:
    print(f"{x} is not an armstrong number.")
