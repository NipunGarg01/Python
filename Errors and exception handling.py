###############################################################################
#
#
#
#  Errors and exception handling.
#  try: execute this code.
#  except:  throw and error if we erros in try.
#  finally:  this piece of code is going to be executed in all cases
#
#
#
#
###############################################################################@@

import random
import logging

def sum(a,b):
    c=a+b
    return c


try:
    sum(4,g)

except NameError:                                          #### Here we can define multiple except according to multiple error types.
    print("You have not passed interger types")

finally:
    print("Hurray")






########################################################################
#
#
#                           Problem 1
#  for in in ["a","b","c"]
#  print(i**2)
#
#   typeError try and except
#
#######################################################################



try:
    for x in ["a","b","c"]:
        print(x**2)

except TypeError:
    print("Strings can not be squared")

finally:
    print("Program execution is done")












########################################################################
#
#                       Problem 2
#
#  x=5
#  y=0
#  z=x/y
#  ZeroDivisonError
#
#######################################################################



try:
    x=5
    y=0
    z=x/y

except Exception as e:
  logging.error("Exception occurred", exc_info=True)


finally:
    print("All done")










########################################################################
#
#                       Problem 3
#
#  x=5
#  y=0
#  z=x/y
#  ZeroDivisonError
#
#######################################################################
































