result :str =""
i=0
def reverse_string(str : str) ->str:
    global result
    global i
    if i<len(str):
        ran=str[len(str) - i - 1]
        result=result+ran
        i+=1
        reverse_string(str)
  
    return result

print(reverse_string("Hello"))