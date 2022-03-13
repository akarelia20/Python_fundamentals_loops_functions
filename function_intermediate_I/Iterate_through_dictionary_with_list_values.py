"""
Create a function printInfo(some_dict) that given a dictionary whose values are all lists,
prints the name of each key along with the size of its list, 
and then prints the associated values within each key's list. For example

7 LOCATIONS
San Jose
Seattle
Dallas
Chicago
Tulsa
DC
Burbank
    
8 INSTRUCTORS
Michael
Amy
Eduardo
Josh
Graham
Patrick
Minh
Devoncopy
"""

dojo = {
    'locations': ['San Jose', 'Seattle', 'Dallas', 'Chicago', 'Tulsa', 'DC', 'Burbank'],
    'instructors': ['Michael', 'Amy', 'Eduardo', 'Josh', 'Graham', 'Patrick', 'Minh', 'Devon']
}

def printInfo(input):
    for key in input.keys():
        print("\n")
        print(f"{len(input[key])} {key.upper()}")
        for value in input[key]:
            print(value)
    
printInfo(dojo) 






