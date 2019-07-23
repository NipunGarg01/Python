class Myclass:
     x=5               #Property named x

P1= Myclass()    # Create an object P1
print(P1.x)








class Person:
    def __init__(self,name,age):       #All classes have a function called __init__(), which is always executed when the class is being initiated.
        self.name=name
        self.age=age


p1=Person("Dipansha",26)
print(p1.name)
print(p1.age)





#Self parameter is for class only and we can use any other name as per our choice , it does not need to be self only.
# Example Below.



class Person:
    def __init__(any_other_than_self,name,age):
        any_other_than_self.name=name
        any_other_than_self.age=age


p1=Person("Dipansha",26)
print(p1.name)
print(p1.age)


#Print the legth of the string.

S=len("Nipun Garg")
print(S)


#Convert all letters to lower case.
#upper is used to to convert in upper case.


S="Nipun Garg"
L=S.lower()
print(L)



#split is used to split the string if it finds seperator

S="Nipun Garg"
S1=S.split()
print(S1)            # returns ['Nipun', 'Garg']




#strip is used to strip the whitespace from beginneing and end

S= " Nipun Garg "
S1=S.strip()
print(S1)            # returns ['Nipun', 'Garg']






#Replacemnet

S="Dipansha Goel"
String="Nipun Garg"
S1=S.replace("Goel","Garg")
S12=String.replace("N","T")                #REPLACEMENT
S13= S.islower()                           #This will return true or false baeed upon all lowercases or uppercases.
print(S12)
print(S1)
print(S13)






#input function , user has to take input from commandline.

if 1:                                    #To execute this code
    print("enter your name")
    N=input ()
    print("user has given name as", N)


if 0:                                      #To block the code.
    print("Dipu")


















































