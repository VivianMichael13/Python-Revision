# Check if a number is prime.

n = int(input("Enter a number: "))
flag = 0
x=n

if n<=1:
    print(f"{n} is not a prime number.")

else:
    for i in range(2,n):
        if n%i==0:
            flag+=1
    if flag>=1:
        print(f"{n} is not a prime number.")
    else:
        print(f"{n} is a prime number.")

