f=open("poems.txt","r")
text=f.read()
print(text)
if("twinkle" in text):
    print("yes")
else:
    print("no")
f.close() 