import module

module.greeting("Jonathan")
a=module.person1["age"]
print(a)



#We can rename a module with as keyword

import module as mx

mx.greeting("Jonathan")
a=mx.person1["age"]
print(a)




import platform

x = dir(platform)
print(x)


## We can only choose to take certain part from any module with from keyword.

from module import person1


