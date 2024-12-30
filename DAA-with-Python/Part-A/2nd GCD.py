n=int(input("Enter number1:"))
m=int(input("Enter number2:"))
ans=0
if n>m:
    for i in range(1,n):
        if n%i==0 and m%i==0:
            ans=i
        else:
                for i in range(1,m):
                    if n%i==0 and m%i==0:
                        ans=i
print("The GCD number is:",ans)
                
