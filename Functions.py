

############################################################################
#DOCSTRING USAGE FOR FUNCTION Definition using

#'''
#'''

############################################################################


def my_function(name):
    '''
    DOCSTRING:   Definition of the function my_function
    Input: name string
    return: My name is <name stringh>
    '''

    return(f'My name is {name}')



x=my_function("Nipun")
print(x)



help(my_function)







#######################################################################
#
#
#    Write a program if the word  starts with vowel , then add ay in the last of the word.
#    Otherwise , return remove the first letter and add that in last followed by ay
#
#######################################################################






def first_letter_check(word):

    '''

    DOCSTRING: This function takes the input as  and perform above operation
    Input:  any word
    Output: changed word
    '''

    if (word[0]== 'a' or 'e' or 'i' or 'o' or 'u'):
        new_word= word+"ay"
    else:
        new_word=word[1:]+word[0]+"ay"

    return new_word


x= first_letter_check("Dipansha")
print(x)

help(first_letter_check)






















