class employee():
    name="Prakhar"
    language="python"

    def getinfo(self):
        print(f"The language is {self.language} and name is {self.name}.")



prakhar=employee()
prakhar.getinfo()
prakhar.salary=1800000 #instance attribute
print(prakhar.salary,prakhar.language)