try:
    a = int(input("Hey, Enter a number: "))
    print(a)

    
except Exception as e:
    print(e) 


else:# this will run  if your try is successful.
    print("I am inside else")
