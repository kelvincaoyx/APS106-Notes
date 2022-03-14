# Get one string from the user, remove all exclamation and question marks 
# from it, and output the resulting string. 
# Do not use any special string methods.

s = input("Please enter a string with question and exclamation marks in it: ")

new_s = ""
i = 0
while i < len(s):
    c = s[i]
    if c != "!" and c != "?":
        new_s += c
    i += 1
        
print(new_s)