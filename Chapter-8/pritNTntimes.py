
cnt=0


def printNtimes(x,N):
    global cnt 
    if cnt==N:
        return
    print(x)
    cnt+=1
    printNtimes(x,N)

printNtimes(3,9)