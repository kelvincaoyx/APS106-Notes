# Prompt the user to enter a string and, using only string 
# comparison functions, decide if the string starts with your first name. 
# If it does, print out “How did you know my name?”. If it doesn’t print out
# “It’s rude to not know my name.”

s = input("Please enter your full name (first<space>last): ")
first_name = "Chris"

if len(s) >= len(first_name) and first_name == s[0:len(first_name)]:
    print("How did you know my name?")
else:
    print("It’s rude to not know my name.")

# Bonus question: why did I check len(s) >= len(first_name)?