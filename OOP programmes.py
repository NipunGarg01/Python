###################################################
#    class Line:
#          def __init__(self, coor1,coor2):
#             pass
#
#    def distance
#
#    def slope
#####################################################





class Line:
    def __init__(self,coord1,coord2):
        self.coord1=coord1
        self.coord2=coord2

    def distance(self):
        return (((self.coord2[1]-self.coord1[1])**2) +  ((self.coord2[0]-self.coord1[0])**2))**0.5

    def slope(self):
        return (self.coord2[1]-self.coord1[1])/(self.coord2[0]-self.coord1[0])



L=Line((2,3),(4,5))
print(L.distance())
print(L.slope())












###################################################
#    class Cylinder:
#          def __init__(self, height,radius):
#             pass
#
#    def volume
#
#    def surface area
#####################################################



class Cylinder:
    pi=3.14
    def __init__(self,height,radius):
        self.radius=radius
        self.height=height



    def SurfaceArea(self):
        '''
        Bulle
        :return:
        '''
        return ((2*(Cylinder.pi)*(self.radius))*((self.radius+self.height)))


    def Volume(self):
        return ((Cylinder.pi)*(self.radius**2)*(self.height))






C=Cylinder(4,2)

print("Volume of the cylinder is {}".format(C.Volume()))
print("Surface Area of the cylinder is {}".format(C.SurfaceArea()))












######################################################################################
#
#
#
#   Challenge:   Create a account class
#                Create a deposit method
#                Create a withdraw method
#
#
#
######################################################################################








class Account:
    def __init__(self,owner,balance=0):
        self.owner=owner
        self.balance=balance


    def withdraw(self,amount_withd):
        if (amount_withd>self.balance):
            print("There is not enough balance in your account !")
        else:
            self.balance=self.balance-amount_withd
            print("{} is deducted from your account".format(amount_withd))

    def deposit(self,amount_depo):
        self.balance=self.balance+amount_depo
        print("Total balance in your account is {}".format(self.balance))


    def __str__(self):
        return (f"Balance of the account holder  {self.owner} is : {self.balance}")





A=Account("Dipansha", 400)
A.withdraw(400)
A.deposit(400)
A.deposit(400)
print(A.balance)
print(A)                    #------------> __str__ will be called from here.



















