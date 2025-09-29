# Generate the Fibonacci sequence up to `n` terms

n = int(input("Enter a number: "))

n1=0
n2=1
n3=n1+n2

print(f"First {n} values of fibonacci sequence are: ")
if n==1:
    print(n1)

elif n==2:
    print(n1)
    print(n2)

else:
    print(n1)
    print(n2)
    for i in range(2,n):
        n3=n1+n2
        print(n3)
        n1,n2=n2,n3