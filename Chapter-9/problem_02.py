def game():
    import random
    score=random.randint(1,100)

    return score

new=game()
with open("hi-score.txt","r") as f:
    data=f.read()
    if(data!=""):
        data=int(data)
    else:
        data=0
    if(data==0 or new>data):
        
        print(data)
        print(new)
        data=new
        print("score is changed")
        print(data)
    else:
        print(data)
        print(new)
        print("no change in hi-score.")


with open("hi-score.txt","w") as f:
    f.write(str(data))

