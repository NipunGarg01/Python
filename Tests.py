###############
#  Problem 1  convert 1024 into binary and hex
#

print(bin(1024))
print(hex(1024))



###################
#
# Problem2 Round 5.32435 to 2 decimal points
#

print(round(5.32435,2))



##########################
#
#  Problem3 check if every letter in string s is lower case
#
#
#

s= "hello how are you Mary, are you feeling okay?"

b=s.islower()

if b== True:
    print("Every letter is lower case")
else:
    print("String contains few upper case letters as well")






###############################
#
#
# Problem4 : Hoe many times letter w show up in string
#

s= "wwwwwwwwwlokjhguttwwwwww,lkjhgvcwwwww"

print(s.count('w'))










##############################
#
# find the elements in set1 which are not in set2
#
#
#

set1= {2,3,1,5,6,8}
set2= {3,1,7,5,6,8}

print(set1.difference(set2))






###########################
#
#  find all elements which are in either set
#
#


print(set1.union(set2))







##############################
#
#
#
# create a dictionary {0:0,1:1,2:8,3:27,4:64} using dictionary comprhension
#
#



d= {x:pow(x,3) for x in range(5)}
print(d)





########################
#
# sort and reverse the list
#
#

list10= [1,2,4,3]
list10.reverse()
print(list10)


list10.sort()
print(list10)


















