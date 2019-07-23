
####################################################################
#
#
#    *args takes n number of arguments and creates a tuple
#     **kwargs args n number of keyword arguments and creates a dictionary
#
#
#
##################################################################



def myfunc(*args):
    '''

    DOCSTRING: This functions takes n number of arguments and sums them

    '''
    print(args)
    sum=0
    for x in args:
        sum=x+sum
        continue
    return sum


d=myfunc(2,3,4)
print(d)
print(type(d))



########################################################################
#
#
#
#
#     Use of **kwagrs ( keywords arguments)   This returns a dictionary
#
#
#
#
#########################################################################





def myfunc_test(**kwargs):
    for x in kwargs:
        print(x)
    return x



s=myfunc_test(name="Nipun", place="Muzaffarnagar",birthday="april")
#print(s)










###############################################################
#
#
#  Define a function which takes n number of arguments and return a list of only even numbers.
#
#
###############################################################



def myfunc1(*args):
    my_new_list= []                     #New list initialization
    for x in args:
        if (x%2==0):
            my_new_list.append(x)
        else:
            continue
    return my_new_list



a=myfunc1(1,2,3,4,5,6,7,8,9,10)
print(a)






###############################################################
#
#
#  Define a function which takes a string and returns a string with even letter is upper case and odd letter is lower case.
#
#
###############################################################







def myfunc2(string):
    index=0
    new_string=""

    for x in string:
        if (index%2==0):
            new_string=new_string+x.upper()
        else:
            new_string=new_string+x.lower()
        index= index+1
    return  new_string



s=myfunc2("Nipun")
print(s)










