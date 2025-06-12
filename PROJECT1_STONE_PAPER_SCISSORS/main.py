'''
stone=-1(s)
paper=0(p)
scissor=1(k)

'''

import random
computer=random.randint(-1,1)

youdict={"s":-1,"p":0,"k":1}
reversedict={-1:"s",0:"p",1:"k"}
yourinput=input("Choose your item : ")
print(f"Computer chooses {reversedict[computer]} you choose {yourinput}")
math=youdict[yourinput]
if(computer==math):
    print("It's draw.")
else:
    if(computer==-1 and math==0):
        print("you wins!")
    elif(computer==-1 and math==1):
        print("you lose!")
    elif(computer==0 and math==1):
        print("you win!")
    elif(computer==0 and math==-1):
        print("you lose!")
    elif(computer==1 and math==-1):
        print("you lose!")
    elif(computer==1 and math==0):
        print("you win!")
    else:
        print("some error is there in the code.")
