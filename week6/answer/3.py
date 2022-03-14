# Write a program that gets the user to enter a string and an integer k 
# such that the length of the string is a multiple of k.
# Chop the string into segments of length k, then print the segments in order
# (separated by a space) with the characters in each 
# segment reversed.
#
# Example
# Please enter the string: University
# Please enter k: 2
# nU vi re is yt


s = input("Please enter the string: ")
k = int(input("Please enter k: "))

# check if k is a factor on n and exit with an error if not
n = len(s)
if n % k != 0:
    print(k, "does not divide evenly into the string length,", n,)
else:
    for i in range(0,n,k):
        substr = s[i:i+k]
        rev_substr = substr[::-1]
        print(rev_substr, end = " ")
    print()
