################################################
#                                              #
#              Conet of function returning function.
#
#
################################################



def Cool():
    print("I am cool")

    def SuperCool():
        print("I am very cool")
    return SuperCool


print(Cool())

new_func= Cool()                    # function assignment to function.
new_func()






#########################
#  Now passing function as an argumnt
#


def Hello():
    return "Hi Nipun!"

def other(some_other_func):
    print("Code reaches here")
    print(some_other_func())




other(Hello)





def new_decorator(my_func):
    def wrap_func():
        print("This code is executed before ")
        my_func()
        print("This code is executed after ")

    return wrap_func

@new_decorator
def function_needs_to_be_decorated():
    print("I want to be decorated")

function_needs_to_be_decorated()                   #--------> This is decorated now.




































