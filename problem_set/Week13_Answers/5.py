def collatz(c1):
    '''
    (int) -> int
    Generates the Collatz sequence and returns the number of elements necessary to reach 1
    '''
    if c1 < 1:
        return None
    
    num_elements = 1
    while c1 > 1:
        num_elements += 1
        if c1 % 2 == 0: # even
            c1 /= 2
        else:
            c1 = 3 * c1 + 1
    
    return num_elements

print(1, collatz(1))
print(55, collatz(55))
print(3, collatz(3))
print(100000000006, collatz(100000000006))

max_len = 0
max_len_start = 0
for i in range(1,10000):
    seq_len = collatz(i)
    if seq_len > max_len:
        max_len = seq_len
        max_len_start = i
    #print(i, seq_len)
print("Max:", max_len_start, max_len)