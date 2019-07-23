my_set= set()
my_set.add(1)          ##-----------> add method
my_set.add(2)
print(my_set)

my_set.clear()         ##-----------> This will clear the set

print(my_set)          ## Here it will return the empty set



s1= {1,2,3,4}
s2={1,2,3}

print(s1.difference(s2))           ## This will return the different element



s1.discard(2)                     ## It will discard 2 from s1
print(s1)




s1.difference_update(s2)               ## will update s1 with difference
print(s1)


s3= {5,6,7}
s4= {5,6}

print(s3.intersection(s4))              ## Will return intersection part

s3.intersection_update(s4)              ## Will update s1 with intersection
print(s3)


s5= {10,11,12}
s6= {12,13,14}
s7 = {10}
s8= {12}

print(s5.isdisjoint(s6))                ## Returns True or false  if two sets are disjoint or not
print(s6.isdisjoint(s7))


print(s8.issubset(s6))                 ## subset : True or False
print(s6.issuperset(s8))               ## Superset : True of False


print(s5.symmetric_difference(s6))     ## Will return the symmentric difference between 2 sets

s5.symmetric_difference_update(s6)     ## This will fill the s5 with symmentric difference
print(s5)






s10= {20,21}
s11= {21,23}
print(s10.union(s11))                  ## This will return the union of two sets

s11.update(s10)                        ## update and union are same
print(s11)



































































