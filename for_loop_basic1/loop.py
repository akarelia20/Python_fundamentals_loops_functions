# Print all integers from 0 to 150.
for x in range(0,151):
    print(x)


# Multiples of Five - Print all the multiples of 5 from 5 to 1,000
for x in range(5,1001,5):
    print(x)


"""
Print integers 1 to 100. 
If divisible by 5,print "Coding" instead. 
If divisible by 10, print "Coding Dojo".
"""
for x in range(1,101):
    if x % 10 == 0: 
        print("Coding Dojo")
    elif x % 5 == 0:
        print("coding")
    else:
        print(x)


# Add odd integers from 0 to 500,000, and print the final sum.
sum = 0
for x in range(0,500001):
    sum += x
print(sum)


# Print positive numbers starting at 2018, counting down by fours
for x in range(2018, 0 , -4):
    print(x)


"""
Set three variables: lowNum, highNum, mult. 
Starting at lowNum and going through highNum, 
print only the integers that are a multiple of mult. 
For example, if lowNum=2, highNum=9, and mult=3, the loop should print 3, 6, 9 (on successive lines)
"""
low_num = 8
high_num = 20
mult = 3
for i in range(low_num, high_num+1):
    if i % 3 == 0:
        print(i) # output : 9,12,15,18




