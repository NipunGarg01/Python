l = [1,2,3]
l.append(4)               # append method
print(l)




l1= [1,2,2,4]
print(l1.count(2))        # Will give you how many values it has 2



#######################
#
# Append Vs Extend method
#


x= [1,2,3]
x.append([4,5])

print(x)                   #    [1, 2, 3, [4, 5]]

### extend will entend the list but will not insert last elemnt as list

x.extend([6,7])
print(x)                   # [1, 2, 3, [4, 5], 6, 7]



if 1 in x:
    print("This list contains 1")


for element in x:
    print(element)



print(x.index(3))                  # This returns the index of the element


x.insert(7,8)                      # insert will insert the element at index position , first is index and second is element
print(x)




x.pop()                            # By default will pop the last element
print(x)

x.pop(0)                           # This will pop the elemnt from 0th index
print(x)





list= [1,2,"inserted", 3,4]
list.remove("inserted")                 ## This method will remove the first occurence of inserted
print(list)


list1= [1,2,3,3,4,5,7]
list1.reverse()                         ## This will reverse the list
print(list1)



z=len(list1)
print(z)




##################
#
# Write a program to remove duplicates from list
#


final_list= []

def Remove(duplicate):
    for x in duplicate:
        if x not in final_list:
            final_list.append(x)

    return final_list


duplicate=[2,4,2,4,3,10,12]
print(Remove(duplicate))







































