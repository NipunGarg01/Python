#############################################################
#
#
#   Regular expressions
#
#
#   .       - Any Character Except New Line
# \d      - Digit (0-9)
# \D      - Not a Digit (0-9)
# \w      - Word Character (a-z, A-Z, 0-9, _)
# \W      - Not a Word Character
# \s      - Whitespace (space, tab, newline)
# \S      - Not Whitespace (space, tab, newline)
#
# \b      - Word Boundary
# \B      - Not a Word Boundary
# ^       - Beginning of a String
# $       - End of a String
#
# []      - Matches Characters in brackets
# [^ ]    - Matches Characters NOT in brackets
# |       - Either Or
# ( )     - Group
#
# Quantifiers:
# *       - 0 or More
# +       - 1 or More
# ?       - 0 or One
# {3}     - Exact Number
# {3,4}   - Range of Numbers (Minimum, Maximum)
#
#
# #### Sample Regexs ####
#
# [a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+
#
#
#
#
#
#
##############################################################





import re


patterns=["term1", "term2"]

text="This is a string with term1, but not the other term"

for x in patterns:
    if re.search(x, text):
        print("Match is found")
    else:
        print("It did not match at all")





#################################################################
##
#
#   Splitting Regular expressions
#
#
#################################################################


My_string= "My email id is ngarg@ciena.com"
print(re.split("@",My_string))                    # This will create a list before and after @


#### Usage of findall

My_string1=" I will win this world, Yes this world"
print(re.findall("world",My_string1))             # This will create a list of matched string





test_phrase= "This is the problem is the"

#  'sd*'       means string starts with s followed by 0  or more d's
#  'sd+'       means string starts with s followed by 1 or more d's
#  'sd?'       means string starts with s followed by 0 or 1 d's
#  'sd{3}      means string starts with s and followed by 3 d's
#  'sd{2,3}'   means string starts with a and followed by 2 or 3 d's


z=(re.findall("wi*", My_string1))
print(z)



# Character Sets
# "[sd]"             means either s or d
# "s[sd]+"         means s followed by one or more s or d

z1= re.findall("[it]",test_phrase)
print(z1)






# Exclusion   use [^....]


My_String3= " I am learning python !#%& right now !"

f=re.findall('[^!#%&]+', My_String3)
print(f)




# Character ranges using -   [a-z] means any letter between a to z


# r"\d+"                    Sequence of digits
# r"\D+"                    Sequence of non-digits
# r"\s+"                    Sequence of white spaces
# r"\S+"                    Sequence of non-white spaces
# r"\w+"                    Sequence of alphanumeric characrs
# r"\W+"                    Sequence of non-alphanumeric characters.































































