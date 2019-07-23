#############################################################
#
#
#
#       Definition of class : class <Nipun>
#
#
#
#
#################################################################



class Dog():
    species="mammal"                                   # This ia class object which is common to this class
    def __init__(self,name, breed, color):
        self.name=name                                 # We can use self.name1 here too but conventionally should not use.
        self.breed=breed
        self.color=color

    def bark(self, number):                            # Method ----> method are functions which are defined in class )   # no need to for self .number as it is parsed from outside
        return("Name of the dog is {} and number is {}".format(self.name, number))







O1=Dog(name="Bruno", breed="Labra", color="brown")
print(O1.breed)
print(O1.name)
print(O1.color)
print(O1.species)







###################################################################################################################################
#
#
#  Methods are defined inside the body of the class
#  Method ----> method are functions which are defined in class   # no need to for self .number as it is parsed from outside
#
##################################################################################################################################


print(O1.bark(45))









###########################################################################
#
#
#   Define a class called circle
#   Define a method under class
#   We can
#
#
###########################################################################




class Circle():

    pi= 3.14

    def __init__(self,radius):
        self.radius= radius
        self.circumferance= 2*(self.radius)*(Circle.pi)                # We can define any attribute here not necessary it has been called from outside like circumferece
                                                                       # Since pi is a class object , we can all it a <class.pi>
    def area(self):
        return ((self.pi)*((self.radius)*(self.radius)))



O2=Circle (3)
print("Area of the circle is {}".format(O2.area()))
print("Circumference of the Circle is {}".format(O2.circumferance))







##############################################################################
#
#
#
#
#
#                              Inheritance
#  Inheritance: Inherit the property of one class into another and use it.
#
#
#
#
################################################################################




class Ciena():
    def __init__(self,domain):
        self.domain=domain

    def Area(self):
        return("Ciena is a {} company".format(self.domain))


class Myclass(Ciena):                           #Inheritance Usage
    def __init__(self,domain):
        Ciena.__init__(self,domain)

    def Area(self):
        return("Ciena is a {} company and I love it".format(self.domain))




O3=Myclass("Telecom")
print(O3.domain)
print(O3.Area())                            # This will call the Area method inside Ciena

# Now if we want to overwrite the method used in inherited class
#   Sample: Add below lines in current class same method with different operation
#
#   def Area(self):
#         return("Ciena is a {} company and I love it".format(self.domain))
#
#
#
















##############################################################################
#
#
#
#
#
#                       Polimorphism
#
#
#
#
#
################################################################################



### Below there are 2 classes which have same definition and have same speak method but both methods returns diferently.

class Lion():
    def __init__(self,name):
        self.name=name


    def speak(self):
        return "{} roars".format(self.name)


class Cat():
    def __init__(self,name):
        self.name=name

    def speak(self):
        return "{} meows".format(self.name)



L= Lion("MYLION")
C= Cat("MYCAT")
print(L.speak())
print(C.speak())


for pat in [L,C]:                               # Listing the objects and iterate through the list
    print(pat.speak())























































