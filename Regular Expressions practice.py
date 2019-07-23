import re

text_to_search = '''
abcdefghijklmnopqurtuvwxyz
ABCDEFGHIJKLMNOPQRSTUVWXYZ
1234567890
Ha HaHa
MetaCharacters (Need to be escaped):
. ^ $ * + ? { } [ ] \ | ( )
coreyms.com
321-555-4321
123.555.1234
123*555*1234
800-555-1234
900-555-1234
Mr. Schafer
Mr Smith
Ms Davis
Mrs. Robinson
Mr. T

ngarg@ciena.com
dipansha.goel@gmail.com
planky2006@gmail.com
nidhi.csit@gmail.com




'''



##### To finc xyz or XYZ

if 0:
    matches = re.findall(r'(x|X)(y|Y)(z|Z)',text_to_search)
    for match in matches:
        print(match)


##To find this pattern in text_to_search
#321-555-4321
#123.555.1234
#123*555*1234
#800-555-1234
#900-555-1234
#
#
#





match1=re.findall(r'(\d{3}[-.*]\d{3}[-.*]\d{4})',text_to_search)

for match in match1:
    print(match)




##############
#
#  write a regular expression to find email address in text_to_search
#



match2=re.findall(r'[a-zA-Z0-9.]+@[A-Za-z0-9]+.[a-zA-Z]+',text_to_search)
print(match2)

for match in match2:
    print(match)



################################
#
#
# Write a regular expression to capture results with Mr or Mr. and then name.
#
#
#


match3=re.findall(r'Mr\.?\s\w*',text_to_search)
print(match3)




#############################
##
#
# Expand aboeb expression to include all Mrs or Mrs.
#



match4=re.findall(r'M[rs.]+\s\w*',text_to_search)
print(match4)

for match in match4:
    print(match)







#####################
#
#
# Write a Python program that matches a string that has an a followed by zero or more b's
#
#



text= ''' 
ddfcascasfdfsdfsd
343532r
sadasdasfaffggzdf_

45364576y
sfasf

abbbbbbbb
cnnn
abbbb
dnn
ab
snnnn
abbbbbbbbbbbbb
a.b
abb
sssss_
dfsgdfgf_
darwerwerefwdfsdv_
Asjkfhaiafug
Sopiorgnfnjfg
kjfybvJkkkkkkkkkkkk
'''


match5= re.findall(r'ab*',text)
print(match5)






#####################################################
#
# Write a Python program that matches a string that has an a followed by one or more b's
#
#


match6= re.findall(r'ab+',text)
print(match6)





#######################################
##
#
#  Write a Python program that matches a string that has an a followed by zero or one 'b'.
#
#

match7= re.findall(r'ab?',text)
print(match7)






##########################################
#
#
# Write a Python program that matches a string that has an a followed by three 'b
#
#



match8= re.findall(r'ab{3}',text)
print(match8)




###########################################
#
#
# Write a Python program that matches a string that has an a followed by two to three 'b'
#



match9= re.findall(r'ab{2,3}',text)
print(match9)






#############################################
#
# Write a Python program to find sequences of lowercase letters joined with a underscore
#
#


match10= re.findall(r'[a-z]+_',text)
print(match10)




#########################################
#
#
# Write a Python program to find sequences of one upper case letter followed by lower case letters
#
#


match11= re.findall(r'[A-Z][a-z]+',text)
print(match11)






#################################################
#
#
# Write a Python program that matches a string that has an 'a' followed by anything, ending in 'b'
#
#

text1= '''Nipun
a*(*&%^*IYHUb
zfdfdwknncab
56hhg Ia*&%b

Dipansha!
'''


match11= re.findall(r'a.*b',text1)
print(match11)



######################################################
#
#Write a Python program that matches a word at the beginning of a string
#
#


match12= re.findall(r'^Nipun',text1)
print(match12)





######################################################
#
# Write a Python program that matches a word at end of string, with optional punctuation
#
#


match13= re.findall(r'Dipansha!?$',text1)
print(match13)






#####################################
#
#
# Write a Python program that matches a word containing 'z
#


text2= '''Nipun
a*(*&%^*IYHUb
zfdfdwknncab
56hhg Ia*&%b
ssaasddxdzdsfdsd
Dipansha!
Crazy dog is lazy enough zig zag  zaz
'''

match14= re.findall(r'\w*z.\w*',text2)
print(match14)






#############################################
#
#
#
#   Write a Python program that matches a word containing 'z', not start or end of the word   ??
#
#




####################################
#
#Write a Python program to match a string that contains only upper and lowercase letters, numbers, and underscores.
#
#


text3= '''
Nipun
Dipansha
3353

lfwdfhfhwgfw
223456789
@#$%^&*
_6756
_afgsv 
'''

match15= re.findall(r'[A-Za-z0-9_]+',text3)
print(match15)










################################
#
#
#
# Write a Python program to remove leading zeros from an IP address
#
#
#


text5= '''
10.10.10.10
20.20.20.20
30.30.30.30
40.40.40.40
01.01.01.01
'''



######################################
#
#
#Write a Python program to check for a number at the end of a string
#



text6= '''
weqwekwefnd
fsd;fsd
12`134567890o
!@#$%^&*(


7989'''


match18=re.findall(r'([0-9]+)$',text6)
print(match18)




################################
#
#
# Write a Python program to search the numbers (0-9) of length between 1 to 3 in a given string
#
#


text7= '''
12345
skdasjkFjf123456
wekqwer345
1234564


'''


match19=re.findall(r'(\d{3})',text7)
print(match19)




################################
#
#
# Write a Python program to search some literals strings in a string
# The quick brown fox jumps over the lazy dog    'fox', 'dog', 'horse'
#



text8= '''

The quick brown fox jumps over the lazy dog 

'''


match20=re.findall(r'(fox|dog|horse)+',text8)
print(match20)




#############################
#
#
#
#Write a Python program to search a literals string in a string and also find the location within the original string where the pattern occurs.
# 'fox'
#




text9= '''

The quick brown fox jumps over the lazy dog

'''


match21=re.search(r'fox',text9)
print(match21)
print(text9[18:21])






####################################
#
#
#
# Write a Python program to find the substrings within a string.
# 'Python exercises, PHP exercises, C# exercises'     find exercises
#



text10= '''
Python exercises, PHP exercises, C# exercises
'''


match22=re.findall(r'(exercises)+',text10)
print(match22)






####################################
#
#
#
# Write a Python program to replace whitespaces with an underscore and vice versa
#
#



text11= 'Python exercises, PHP exercises, C# exercises'
match23=re.sub(r'[\s]+',"_",text11)                              #------------->  using re.sub method
match24=re.sub(r'[_]+'," ",match23)                              #-------------> using re.sub method to convert back
print(match24)





#############################
#
#
#Write a Python program to extract year, month and date from a an url
#
#
#



url1= "https://www.washingtonpost.com/news/football-insider/wp/2016/09/02/odell-beckhams-fame-rests-on-one-stupid-little-ball-josh-norman-tells-author/"
match25=re.findall(r'\d{4}/\d{2}/\d{2}',url1)
print(match25)





#################################
#
#
#
# Write a Python program to match if two words from a list of words starting with letter 'P'
#
#
#


text14= ["Python PHP", "Java JavaScript", "c c++"]

for t in text14:
    w=re.match(r'(P[\w]+)\W(P[\w]+)',t)
    if w:
        print(w.groups())                # returns a tuple.







###
#
#
#   Write a Python program to find all words starting with 'a' or 'e' in a given string
#
#
#
#

text15= '''
asbbbbbb
emmmmmmm

!@#$%^&*(
abraham
emli abdeliers

'''

match18=re.findall(r'([ae]\w+)',text15)
print(match18)





###########################################
#
#
#
#Write a Python program to separate and print the numbers of a given string with thei positions
#
#
#


text16='''
1
2
4
4
34567
1
321
2r
24r
24r
asdfghjkl
2e
dwef
a;vlfw7dtegcb
345678


'''



match19=re.finditer(r'\d+',text16)
print(match19)

for match in match19:
    print(match.start())              # we can use span() to see tha range






############################
#
#
# Write a Python program to abbreviate 'Road' as 'Rd.' in a given string
#
#
#


text17='''
Akbar Road
Lodi Road
Loni Road
Pratap Road


'''


match20=re.sub(r'Road',"Rd",text17)
print(match20)






########################
#
#
#
# Write a Python program to replace all occurrences of space, comma, or dot with a colon.
#
#


text18='''
My Name is Anthony G Salvis
I am alone in this, world
This is Nipun.Garg

'''


match21=re.sub(r'[\s.,]+',":",text18)
print(match21)










########################
#
#
#
# Write a Python program to replace max 2  occurrences of space, comma, or dot with a colon
#
#


text18='''
My Name is Anthony G Salvis
I am alone in this, world
This is Nipun.Garg

'''


match21=re.sub(r'[\s.,]+',":",text18,2)
print(match21)





#######################################
#
#
#
# Write a Python program to find all five characters long word in a string
#
#


text19='''
My Name is Anthony G Salvis
I am alone in this, world
This is Nipun Garg

'''


match22=re.findall(r'\b[\w]{5}\b',text19)
print(match22)






#########################
#
#
# Write a Python program to find all three, four, five characters long words in a string
#
#


text20='''
My Name is Anthony G Salvis
I am alone in this, world and you are alone aswell
This is Nipun Garg

'''


match23=re.findall(r'\b[\w]{3,5}\b',text20)
print(match23)








##################################
#
#
# Write a Python program to find all words which are at least 4 characters long in a string
#
#


text21='''
My Name is Anthony G Salvis
I am alone in this, world and you are alone aswell
This is Nipun Garg

'''


match24=re.findall(r'\b[\w]{4,}\b',text21)
print(match24)







######################################
#
#
#  Write a Python program to extract values between quotation marks of a string
#
#


text28= '''
I am the "best"
"Cool"
hhjjjhjjghj"Super"
@#$%"Nipun"
"1234"
'''
match28=re.findall(r'"([\w]+)"',text28)
print(match28)






#################################
#
#
#
# Write a Python program to remove multiple spaces in a string
#
#



text29= '''
I am the                "best"
"Cool"
hhjjjhjjghj"Super"
@#$%"Nipun"
"1234"
'''
match29=re.sub(r'\s{2,}'," ",text29)
print(match29)






#################################
#
#
#
# Write a Python program to remove all whitespaces in a string
#
#


text30= '''
I am the                "best"
"Cool"
hhjjjhjjghj"Super"
@#$%"Nipun"
"1234"
'''
match30=re.sub(r'\s+',"",text30)
print(match30)






############################################
#
#
#
# Write a Python program to remove everything except alphanumeric characters from a string
#
#



text31= '''
I am the best
"Cool"
hhjjjhjjghj"Super"
@#$%"Nipun"
"1234"
'''
match31=re.sub(r'\W+',"",text31)
print(match31)







############################################
#
#
#
# Write a Python program to find urls in a string.   ?
#
#






################################
#
#
#
# Write a Python program to remove words from a string of length between 1 and a given number
#
#


text32= '''
tfdeqska;lcn
asdajjcb
Nipun is the cool guy
He is working with Ciena India Private limited.


'''


match32= re.sub(r'\b\w{1,3}\b',"",text32)
print(match32)




###################################
#
#
#
#  Write a Python program to remove the parenthesis area in a string
#  Sample data : ["example (.com)", "w3resource", "github (.com)", "stackoverflow (.com)"]
# Expected Output:
# example
# w3resource
# github
# stackoverflow
#



items = '''
"example (.com)", "w3resource", "github (.com)", "stackoverflow (.com)"
'''

match33=re.sub(r'\t?\([^)]+\)',"",items)
print(match33)






###############################
#
#
#
#Write a Python program to insert spaces between words starting with capital letters.
#








































