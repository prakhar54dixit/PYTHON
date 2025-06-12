#sum of first n natural numbers using recursion.
def sum(n):
    if(n==1):
        return 1
    return n+sum(n-1)

print(sum(10))