age : int =23 #hinting python that age is of integer data type.(:) is used here.

def greet(name :str) -> str: #  (->) is used for indiacting return type of function.
    return f"hello ! {name}"

print(greet("Prakhar"))
