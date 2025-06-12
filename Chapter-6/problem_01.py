a1=int(input("Enter the number : "))
a2=int(input("Enter the number : "))
a3=int(input("Enter the number : "))
a4=int(input("Enter the number : "))
# ls=[a1,a2,a3,a4]
# ls.sort()
# ls.reverse()
# print(ls[0])

if(a1>a2 and a1>a3 and a1>a4):
    print(f"{a1} is greatest. ")

elif(a2>a3 and a2>a1 and a4>a4):
    print(f"{a2} is greatest. ")

elif(a3>a2 and a3>a1 and a3>a4):
    print(f"{a3} is greatest. ")

else:
    print(f"{a4} is greatest.")