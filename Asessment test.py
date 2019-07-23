#################################################################################################

#Use for, .split(), and if to create a Statement that will print out words that start with 's':
# st = 'Print only the words that start with s in this sentence'

#################################################################################################


st='Print only the words that start with s in this sentence'

splitted_list= st.split()
print(splitted_list)

for x in splitted_list:
    if (x[0]== "s"):
        print(x)
    else:
        continue







#################################################################

# Use range() to print all the even numbers from 0 to 10.

################################################################


my_range=list(range(0,10))
print(my_range)



for x in my_range:
    if (x%2==0):
        print(x)
    else:
        continue






#######################################################################################################
#Use a List Comprehension to create a list of all numbers between 1 and 50 that are divisible by 3.

# Go through the string below and if the length of a word is even print "even!"

######################################################################################################



st1 = "Print every word in this sentence that has an even number of letters"
my_splitted_list1= st1.split()
print(my_splitted_list1)


for x in my_splitted_list1:
    if (len(x)%2==0):
        print("even!")
    else:
        continue





########################################################

#Write a program that prints the integers from 1 to 100. But for multiples of three print "Fizz" instead of the number, and for the multiples of five print "Buzz". For numbers which are multiples of both three and five print "FizzBuzz".

########################################################


my_range= list(range(1,101))
print(my_range)

for x in my_range:
    if (x%15==0):
        print(f'value of x is {x} FizzBuzz')
    elif (x%3==0):
        print(f'value of x is {x} Fizz')
    elif (x%5==0):
        print(f'value of x is {x} Buzz')
    else:
        continue











































