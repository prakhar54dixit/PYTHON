#Sometimes we need a function that does not use the self-parameter. We can define a
# static method like this:
class employee():
    name="Prakhar"
    language="python"

    @staticmethod # decorator to mark greet as a static method
    def greet():
        print("Hello user")



prakhar=employee()
prakhar.salary=1800000 #instance attribute
print(prakhar.salary,prakhar.language)