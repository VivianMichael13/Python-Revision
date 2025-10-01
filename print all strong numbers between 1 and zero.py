# print all strong numbers (sum of factorial of digits = number) between 1 and 1000

for i in range(1,1001):
    j=i
    sum=0
    temp = i
    while temp>0:
        fact=1
        dig = temp%10
        for k in range(1,dig+1):
            fact*=k
        sum+=fact
        temp = temp//10

    
    if sum==j:
        print(j)