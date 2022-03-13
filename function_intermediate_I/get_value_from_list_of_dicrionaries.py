"""
a function iterateDictionary2(key_name, some_list) that, 
given a list of dictionaries and a key name, 
the function prints the value stored in that key for each dictionary. For example, 
iterateDictionary2('first_name', students) should output:
Michael
John
Mark
KB
copy
"""

students = [
        {'first_name':  'Michael', 'last_name' : 'Jordan'},
        {'first_name' : 'John', 'last_name' : 'Rosales'},
        {'first_name' : 'Mark', 'last_name' : 'Guillen'},
        {'first_name' : 'KB', 'last_name' : 'Tonel'}
    ]

def iterateDictionary2(key_name, some_list):
    result= ""
    for i in range(0,len(some_list)):
        result += f"{(some_list[i].get(key_name))} \n"
    return result
print(iterateDictionary2('first_name', students))
print(iterateDictionary2('last_name', students))

