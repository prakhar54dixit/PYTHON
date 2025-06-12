# elif ladder
a=int(input("Enter your age : "))
if(a<=0):
    print("You are entering a invalid age.")
elif(a<18):
    print("You are below the age of consent.")
else:
    print("You are above the age of consent.")