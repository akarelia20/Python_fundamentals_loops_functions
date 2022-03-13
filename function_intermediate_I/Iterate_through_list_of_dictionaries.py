'''
function iterateDictionary(some_list) that, given a list of dictionaries, 
the function loops through each dictionary in the list and prints each key and the associated value. 
OUTPUT:
first_name - Michael, last_name - Jordan
first_name - John, last_name - Rosales
first_name - Mark, last_name - Guillen
first_name - KB, last_name - Tonel
'''

students = [
        {'first_name':  'Michael', 'last_name' : 'Jordan'},
        {'first_name' : 'John', 'last_name' : 'Rosales'},
        {'first_name' : 'Mark', 'last_name' : 'Guillen'},
        {'first_name' : 'KB', 'last_name' : 'Tonel'}
    ]
def iterateDictionary(input): 
    for i in range (0, len(input)):
        result= ""
        for key,value in input[i].items():
            result += f" {key} - {value},"
        print(result)
(iterateDictionary(students))


