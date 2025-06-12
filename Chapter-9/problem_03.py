def table(n):
    i=1
    while i<11:
        print(f"{n}*{i}={n*i}")
        i+=1

n=2
while n<21:
    f=open(f"{n}.txt","w")
    f.write(str(table(n)))

    n+=1
    f.close()