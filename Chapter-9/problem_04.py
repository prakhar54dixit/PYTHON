word="Donkey"
with open("file.txt","r") as f:
    data=f.read()

datanew=data.replace(word,"####")
with open("file.txt","w") as f:
    f.write(datanew)

    
