a=int(input("Enter marks in subject-1 :"))
b=int(input("Enter marks in subject-2 :"))
c=int(input("Enter marks in subject-3 :"))
s=(a+b+c)/3
if(a<33 or b<33 or c<33):
    print("Bhai tu fail hai !")
elif(s>=40):
    print("bch gya bhai !")
else:
    print("bhagg yha se !! Fail.")