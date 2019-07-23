

"""
MAP Function
This is used when we want to iterate through some list or string etc and wants to apply same func on all list values or
string letters etc.

Takes func as argument
"""


def my_func(number):
    return number**2

my_list = [1,2,3,4,5,6]

print(map(my_func,my_list))

for x in map(my_func,my_list):
    print(x)





def splicer(x):
    if len(x)%2 == 0:
        return "Even"
    else:
        return x[0]

my_list1 = ["Nipun", "Nidhi", "Dipansha", "Gudda"]


print(list((map(splicer,my_list1))))

for x in map(splicer,my_list1):
    print(x)





"""
Filter Function 
"""


def check_even(num):
    return num%2 == 0

my_num_list = [1,2,4,6]
print(list(filter(check_even,my_num_list)))

for x in filter(check_even,my_num_list):
    print(x)






"""
LAMBDA Expression 

We can assign any lammda expression to func
"""


my_lambda_func = lambda num:num%2 == 0

for x in filter(my_lambda_func,my_num_list):
    print(x)


for x in filter (lambda num:num%2 == 0, my_num_list):
    print(x)







