import random
##############################
#
#  To save memory
#  it picks from last result              YIELD keyword
#


def create_cubs(n):
    for x in range(n):
        print(x**3)

create_cubs(100)

#OR  I can use yield word


def create_cubs1(n):
    for x in range(n):
        yield x**3

create_cubs1(10)






def simple_generator():
    for x in range(4):
        yield x

g= simple_generator()
print(g)   #----------> Generator object

print(next(g))          # This will print 0
print(next(g))          # This will print 1
print(next(g))          # This will print 2
print(next(g))          # This will print 3
#print(next(g))          # Will not print anything as iteration is over.








##################################
#
#  Exercise: Create a generator to generate the square of number upto number N
#
#



def my_generator(n):
    for x in range(n):
        yield x**2


for x in my_generator(4):
    print(x)





###################################
#
#  s= "Hello"
#  convert s here into iterator
#



s= "hello"
s1=iter(s)
print(s1)





################################
#
#
#    random function returns  n random numbers between low and high
#
###################################



def rand_rum(low,high,n):
    for i in range(n):
        yield random.randint(low,high)


for x in rand_rum(1,10,12):
    print (x)






















