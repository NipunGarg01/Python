############################################
#
#
#      Counter module
#
#
#############################################



from collections import Counter

l= [1,1,1,1,1,2,2,2,2,2,4,4,4,4,5,6,6,8]

x=Counter(l)        #--------------> This will create a dictonary of numbers with repeation and present it in tuple
print(x)


string="NipunNipunNipunNipunGarg"
y=Counter(string)

print(y)






my_string= "How many times word is hit word word word word baby how many times is"

my_splitted_string= my_string.split()
print(my_splitted_string)

counters_application=Counter(my_splitted_string)               ###----------------> Counter application in list
print(counters_application)


print(counters_application.most_common(3))                    ####-----------------> .most_common(n) will tell you mostly used words.


print(sum(counters_application.values()))                     ####-----------------> This will give us the sum of values.



###########
#
#
# list(c)  will convert into list of unique elements
# set(c)   convert to a set
# dict(c)  convert to a regular dictionary
#



print(list(counters_application))
print(dict(counters_application))


print(counters_application.items())      #####--------> This will convert into a list of element count pair tuples



print(counters_application.clear())      #####---------> Reset all counts











################################################################
#
#
#
#                defaultdict
#
#
#################################################################


from collections import defaultdict
dict1= {'Name': 'Nipun'}

print(dict1)
print(dict1['Name'])       ##-------> This will print value of key Name

#print(dict1['Age'])        ###----->  There is no key as Age and it will throw Key error.





dict2= defaultdict(object)

dict2['Name']                 ###----------------> This will assign Name key to dict2

for item in dict2:
    print(item)              ### ---------------> This will print the key.



####

dict3= defaultdict(lambda : 0)                       ## Using lambda function which will return always 0

print(dict3['Name'])                                 ## Now this will return 0


dict3['Age'] = 32

print(dict3)                                         #### Lambda function will return 0 for all unassigned keys
















############################################################
#
#
#
#
#        Ordered dictionary
#
#
#
#############################################################


############################
# first example of normal dictionary
#
###########################

print(" Normal Dictionary :")

d = {}


d['Name'] = 'Nipun'
d['Age']  = '32'
d['Place'] = 'Muzaffarnagar'
d['Company'] = 'Ciena'

print(d)


for x,y in d.items():
    print (x, y)                       #-----------------> This does not guarantee that items will be printed in ordered fashion.



#######


from collections import OrderedDict


d1= OrderedDict()



d1['Name'] = 'Nipun'
d1['Age']  = '32'
d1['Place'] = 'Muzaffarnagar'
d1['Company'] = 'Ciena'


for x,y in d1.items():
    print (x, y)


print(d==d1)          ##---------> This will retun True since key and values are added in same order but return false when order is changed.






#################################
#
#
#
#   Namedtuple
#
#



from collections import namedtuple

## Normal Tuple.

t= (1,2,3)
print(t[0])


###############
##
# Create a namedtuple ( first is like class name a dog and then other self ... like name  age and breed
# Creates a new object type
#

Dog = namedtuple('Dog', 'name age breed')

sam= Dog(name="sammy", age="10", breed="labra")

print(sam)
print(sam.name)
print(sam.age)
print(sam.breed)








































