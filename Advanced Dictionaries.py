d= {"k1":1 ,"k2":2}
print(d)





############################################
#
#  Create a dictionary in same {}
#
#

d1={x:pow(x,2) for x in range(10)}

print(d1)

for k in d.items():                    ### This will return tuple of each item
    print (k)

for k in d.values():                  ### This will return values of each key
    print(k)

for k,v in d:                         ### This will print each key and value
    print( k, v)



for k in d.keys():
    print(k)















