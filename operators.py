#range function


for x in range(10):              # not including 10
    print(x)


for x in range(1,11,2):
    print(x)


my_list=list(range(1,11,2))
print(my_list)



index =0

for letter in "Nipun":
    print(f'index at position {index} is {letter}')
    index = index+1



my_word="Dipansha"

#enumerate function.

for my_index,letter in enumerate(my_word):
    print(letter)
    print(my_index)

# enumerate function will create a tuple.



my_converted_list=list(enumerate("Nipun Garg"))                # This will create a list of tuples.
print(my_converted_list)



# Zip function, zips the lists together.

my_list1= [1,2,3]
my_list2= [5,6,7]


my_zipped_list=  zip(my_list1+my_list2)  # Basically this returns the tuple.
my_zipped_list1= zip(my_list1,my_list2)  #This returns the tuple.

print(*my_zipped_list)
print(*my_zipped_list1)         #accessing the memory using *









for index,tuplepair in enumerate(zip(my_list1,my_list2)):
    print(f'Tuple at index {index} is {tuplepair}')



my_dict= {
    "Car"               : "Swift",
    "Registration"      : "Gurgaon",
    "Color"             : "Light Brown"
}


for x in my_dict.values():
    print(x)

for x in my_dict.keys():
    print(x)




# min and max keywords.

my_num_list= [1,2,3,4,5]
m=min(my_num_list)
m1=max(my_num_list)

print(m)
print("\n",m1)
print(m1)







LIST= [1,2,3,4,5,6]

#z=randint(1,10)



























































































