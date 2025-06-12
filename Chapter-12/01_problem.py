
try:
    with (open ("file1.txt") as f1):
        data=f1.read()
except Exception as e:
    print(e)
try:
    with (open ("file2.txt") as f2):
        da=f2.read()
except Exception as e:
    print(e)
try:
    with (open ("file3.txt") as f3):
        dat=f3.read()
except Exception as e:
    print(e)