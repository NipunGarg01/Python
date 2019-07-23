
from __future__ import print_function
x =0

while (x<5):
    if (x==5):
        break                                 # Using break , comes out of loop.
    print(f'The current value of x is {x}')
    x+=1

print (f'The current value of x is {x}')



y=1

while (y<=20):
    if (y%2==0):
        print(f'{y} is the even number')
        y=y+1
    else:
        print(f'{y} is the odd number')
        y=y+1


for i in range(1, 5):
    for j in range(i):
         print(i, end=' ')
    print()















