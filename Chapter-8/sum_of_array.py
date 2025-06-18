sum=0
i=0
def accumulate(arr:list):
    global sum,i
    if i<len(arr):
        sum=sum+arr[i]
        i+=1
        accumulate(arr)
        
    return sum
    
    
print(accumulate([3,4,5,6,1,2]))