#Python Collections (Arrays)
#There are four collection data types in the Python programming language:

#List is a collection which is ordered and changeable. Allows duplicate members.
#Tuple is a collection which is ordered and unchangeable. Allows duplicate members.
#Set is a collection which is unordered and unindexed. No duplicate members.
#Dictionary is a collection which is unordered, changeable and indexed. No duplicate members.
#When choosing a collection type, it is useful to understand the properties of that type. Choosing the right type for a particular data set could mean retention of meaning, and, it could mean an increase in efficiency or security.



# list can be a combination of different data types. example :   ["Nipun",3,4.5]

#LIST is LIFO

mylist= ["Nipun","Dipansha","Shravya","Mamtesh","Rameshwar"]
print(mylist)
mylength=len(mylist)
print(mylength)                     #to determine length of list
print(mylist[4])                    #to print specific element


#clearlist=mylist.clear()            #to clear the list
#print(clearlist)

for x in mylist:
    print(x)


if "Shravya" in mylist:
    print("yes, shravya is in this list")


## Use append to add the element in the last of the list.


mylist.append("Nidhi")
print(mylist)



## Insert the item at specified index.

mylist.insert(1,"Pankhu")
print(mylist)



## To remove item from list

mylist.remove("Pankhu")
print(mylist)



##Del keyword can delete the entire list or specifc index

mylist.insert(1,"Pankhu")
print(mylist)
del mylist[0]
print(mylist)
#del mylist            #This will delete the entire list
print(mylist)
mylist.insert(0,"Nipun")
print(mylist)



## Clear will clear the list


#mylist.clear()
print(mylist)



# To sort the list

mylist.sort()
print(mylist)


# To Reverse the list

mylist.reverse()
print(mylist)



# Pop the elelemt at specified element


mylist.pop(0)
print(mylist)



# index returns the index.

i=mylist.index("Mamtesh")
#print(i)
print(mylist.index("Mamtesh"))



#Count word return the value of specified item in list itself.

mylist2=["Nipun", "Nipun", "nipun"]
print(mylist2.count("Nipun"))


























































