#prime or not.
m=0
n=int(input("Enter the number : "))
for i in range(1,n+1):
    if(n%i==0):
        m+=1

if(m==2):
    print("Prime number.")
else:
    print("Not a prime number.")