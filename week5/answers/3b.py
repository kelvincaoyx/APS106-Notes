# Prompt the user to enter a string and, using only string 
# comparison functions, decide if the string starts with your first name. 
# If it does, print out “How did you know my name?”. If it doesn’t print out
# “It’s rude to not know my name.”

#b) Write a function that takes two strings and returns True if the two “match”, where this
#time “matching” is not case sensitive. (So “Smith” and “smitH” match). Redo part a) using
# this function.

def string_match(s1, s2):
    '''
    (str, str) -> bool
    Returns True of the strings are identical. Not case sensitive.
    '''
    return s1.lower() == s2.lower()

s = input("Please enter your full name (first<space>last): ")
first_name = "chris"

if len(s) >= len(first_name) and string_match(first_name, s[0:len(first_name)]):
    print("How did you know my name?")
else:
    print("It’s rude to not know my name.")

# Bonus question: why did I check len(s) >= len(first_name)?