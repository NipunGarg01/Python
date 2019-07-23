#    A dictionary is a collection which is unordered, changeable and indexed. In Python dictionaries are written with curly brackets, and they have keys and values.



thisdict =	{
  "brand": "Ford",
  "model": "Mustang",
  "year" : 1964
}

print(thisdict)


x=thisdict["model"]
print(x)


#printing individual keys
#Loop Through a Dictionary
#You can loop through a dictionary by using a for loop.

#When looping through a dictionary, the return value are the keys of the dictionary, but there are methods to return the values as well.


for x in thisdict:
    print(x)


#accessing elements

for x in thisdict:
    print(thisdict[x])





#looping both keys and values using items function.


for x,y in thisdict.items():
    print(x,y)



if "model" in thisdict:
    print("yes, 'model' is one of the keys")




#length printing   , how many key-value pair exists.

x=len(thisdict)
print(x)




#new item addition.

thisdict["color"]="red"

print(thisdict)



#removing specific key

thisdict.pop("model")
print(thisdict)



#The del keyword removes the item with the specified key name:


del thisdict["color"]
print(thisdict)



# To empty the dictionary

thisdict.clear()
print(thisdict)




# It is also possible to use the dict() constructor to make a dictionary:

thisdict =	dict(brand="Ford", model="Mustang", year=1964)
print(thisdict)



##################
# Dictionary can cntain lists as well as other dictionaries too.

D={
    "Company" : "Maruti" ,
    "Car"   :    "SWIFT Dzire",
    "Accessory" : ["Stearing", "GearLock" , "musicSystem"],
    "Another Dictionary"  : {"Name": "Nipun", "Age": 32, "Place": "Muzaffarnagar" }
}

print(D)         #Print the entire dictionary


# Printing key values

print(D["Company"])
print(D["Accessory"][2])
print(D["Another Dictionary"]["Place"])




# .keys and .values returns keys and values.


print(D.keys())
print(D.values())
print(D.items())




thisdict1 =	{
  "brand": "Ford",
  "model": "Mustang",
  "year" : 1964
}

thisdict2 =	{
  "brand": "Ford",
  "model": "Mustang",
  "year" : 1964
}



#dict_concatenated= thisdict1+thisdict2                 #Dictionary can not be concatenated.
#print(dict_concatenated)




thisdict10 =	{
  "brand": { 'my' : '2'},
  "model": "Mustang",
  "year" : 1964
}

for x, y in thisdict10.items():
    print(y)
    
    #print(x)
print(thisdict10.keys())





















