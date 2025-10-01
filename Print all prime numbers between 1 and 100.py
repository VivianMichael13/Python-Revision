# Print all prime numbers between 1 and 100.



for i in range(3,101):
    flag=0
    for j in range(2,i):
        if i%j==0:
            flag+=1
    if flag==0:
        print(i)