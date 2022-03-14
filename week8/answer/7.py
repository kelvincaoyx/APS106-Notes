# Q11 from P. 221 Gries book

    
def sparse_add(vector1, vector2):
    """ (dict of {int: int}, dict of {int: int} -> dict of {int: int})

    Return the sum of sparse vectors vector1 and vector2.

    >>> sparse_add({1: 3, 3: 4}, {2: 4, 3: 5, 5: 6})
    {1: 3, 2: 4, 3: 9, 5: 6}
    """ 

    sum_vector = vector1.copy()

    # if there is an element in both, add them
    # if the element is only in vector2, insert it into the sum_vector
    for key in vector2:
        if key in sum_vector:
            sum_vector[key] = sum_vector[key] + vector2[key]
        else:
            sum_vector[key] = vector2[key]

    return sum_vector


def sparse_dot(vector1, vector2):
    """ (dict of {int: int}, dict of {int: int} -> dict of {int: int})

    Return the dot product of sparse vectors vector1 and vector2.

    >>> sparse_dot({1: 3, 3: 4}, {2: 4, 3: 5, 5: 6})
    20
    """ 

    dot = 0
    # if there is an entry in both, multiply
    # if not entry in both, ignore (since multiplication will be 0)
    for key1 in vector1:
        if key1 in vector2:
            dot += vector1[key1] * vector2[key1]

    return dot

def sparsify(list):
    ''' (list of int) -> dict of {int: int}
    Returns the sparse vector version of list
    '''
    vec = {}
    # add all non-zero entries to the sparse vector
    for i in range(len(list)):
        if list[i] != 0:
            vec[i] = list[i]
            
    return vec

def re_sparsify(sparse_vec):
    ''' (dict of {int: int}) -> dict of {int: int}
    Returns sparse_vec with any 0 entries removed
    '''
    vec = {}
    # add all non-zero entries to the new sparse vector
    for k, v in sparse_vec.items():
        if v != 0:
            vec[k] = v
            
    return vec


v = sparsify([1,0,0,0,0,0,3,0,0,0])
sum_vec = sparse_add(v,v)
print(v)
print(sum_vec)

sub_vec = sparsify([1,0,0,0,0,0,-6,0,0,0])
sum2_vec = sparse_add(sum_vec, sub_vec)
re_sparse = re_sparsify(sum2_vec)

print(sub_vec)
print(sum2_vec)
print(re_sparse)

print(sparse_add(sparsify([0,0,1,-2,0,0]), sparsify([0,1,0,2,0,0])))
