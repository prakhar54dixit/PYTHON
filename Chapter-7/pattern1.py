n = int(input("Enter the number: "))
i = 1
while i < n + 1:
    print(" "*(n-i),end="")
    print("*"*(2*i-1),end="")
    print("")
    i+=1
