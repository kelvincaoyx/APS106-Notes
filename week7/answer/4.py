# Write a program that gets the user to enter a string and an integer k 
# such that the length of the string is a multiple of k.
# Chop the string into segments of length k, then print the segments in the 
# reverse order (separated by a space) and also the characters in each 
# segment reversed.
#
# Example
# Please enter the string: University
# Please enter k: 2
# yt is re vi nU

def chop_up_string(s,k):
    ''' (str, int) -> list
    Returns a list of substrings of s of length k. Assumes that len(s)/k is
    an integer
    '''
    substrings = []
    for i in range(0,n,k):
        substr = s[i:i+k]
        substrings.append(substr)

    return substrings

s = input("Please enter the string: ")
k = int(input("Please enter k: "))

# check if k is a factor on n and exit with an error if not
n = len(s)
if n % k != 0:
    print(k, "does not divide evenly into the string length,", n,)
else:
    substrings = chop_up_string(s, k)

    # reverse list since we need to print the substrings in reverse order

    for sub_str in reversed(substrings):
        # print each substring reversed
        print(sub_str[::-1], end=" ")
