class employee():
    name="Prakhar"
    language="python"
    salary=1400000

prakhar=employee()
prakhar.salary=1800000 
print(prakhar.salary,prakhar.language)
# Note: Instance attributes, take preference over class attributes during assignment &
# retrieval.
# When looking up for harry.attribute it checks for the following:
# 1) Is attribute present in object?
# 2) Is attribute present in class?
