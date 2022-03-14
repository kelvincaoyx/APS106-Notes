# Ask the user for an integer and output the “flipped” version. 
#
# For example:
# Enter a positive number: 17709
# That number flipped is 90771
#
# You should write two different programs to do this:
# 1. Convert the user’s input as a string and investigate the 
#    string methods to do it.
# 2. Represent the user’s input as a integer and use the arithmetic 
#    operators to do it.

# string version 1
def flip_number_string(num):
    '''(int) -> int
    Return the integer with its digits reversed 
    '''
    s = str(num)
    # uses extended slicing syntax 
    # (see https://stackoverflow.com/questions/931092/reverse-a-string-in-python)    
    return int(s[::-1]) 


# string version 1
def flip_number_int(num):
    '''(int) -> int
    Return the integer with its digits reversed 
    '''

    flipped = 0
    while num > 0:   
        ones_digit = num % 10
        num //= 10
        flipped = 10 * flipped + ones_digit
        #print(ones_digit, num, flipped)
        
    return flipped


num = int(input("Enter a positive integer: "))

print("String version: ", flip_number_string(num))

print("Int version: ", flip_number_int(num))

