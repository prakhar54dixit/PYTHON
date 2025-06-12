import random
a=random.randint(1,10)
score=1
b=int(input("Enter the number : "))
while b!=a :
    if(b<a):
        print("Higher number please.")
        score+=1
        b=int(input("Enter the number again: "))
    else:
        print("Lower number please.")
        score+=1
        b=int(input("Enter the number again: "))

print(f"you won! your score is {score}.")