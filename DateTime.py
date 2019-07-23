import datetime


t = datetime.time (5,25,1, 45)             # 5 is hour 25 is minutes 1 is seconds 45 is microseconds
print(t)

print(t.hour)
print(t.minute)
print(t.second)
print(t.microsecond)


print(datetime.time.min)              ####--------> Min time 00:00:00
print(datetime.time.max)              #### --------> Max time 23:59:59.99999999




print(datetime.time.resolution)       #### -------> resolution of 0:00:00.000001




######################
#
# date
#


today = datetime.date.today()
print(today)                           ####-----> This gives value in year-month-day format


print(today.year)
print(today.month)
print(today.day)





d1=datetime.date(1987,4,7)
print(d1)

print(d1.year)
print(d1.month)
print(d1.day)


######## I can also use replace method
#
# Lets change the year month and day of d1
#


d2= d1.replace(year=1988,month=5, day=9)
print(d2.year)
print(d2.month)
print(d2.day)






#####################
#
#  We can also check arithmetic

d3=d2-d1
print(d3)           ###-----------> This will show you the days difference in two dates













































