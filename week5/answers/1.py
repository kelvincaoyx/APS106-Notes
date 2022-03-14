
#1 Read one string from the user. Then, swap cases and print the result. 
# In other words, convert all lowercase letters to uppercase letters and 
# vice versa. 
# You should solve this question twice.
# a) There is a str method that will do this for you and so after the input 
#    just call it.
# b) But a) is not much of an exercise, so you should also do it without 
#    calling that function!

s = input("Please input a string with upper and lower case letters: ")

# Do it with the str method swapcase
print(s.swapcase())

# Now do it "by hand" without calling swapcase
i = 0
while i < len(s):
    ch = s[i]
    if ch.islower():
        new_ch = ch.upper()
    else:
        new_ch = ch.lower()
        
    print(new_ch, end='')
    i += 1

print('')