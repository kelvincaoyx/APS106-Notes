# Q2 from p. 219 of Gries book
# Using the set.pop() method write a function called mating_pairs 
# that takes two equal-sized sets called males and females as input and 
# returns a set of pairs; each pair must be a tuple containing one male and 
# one female. (The elements of males and females may be strings containing 
# gerbil names or gerbil ID numbers — your function must work with both.)

def mating_pairs(males, females):
    """ (set, set) -> set of tuple

    Return a set of tuples where each tuple contains a male from males and a 
    female from females.

    >>> mating_pairs({'Anne', 'Beatrice', 'Cari'}, {'Ali', 'Bob', 'Chen'})
    {('Cari', 'Chen'), ('Beatrice', 'Bob'), ('Anne', 'Ali')}
    """ 

    pairs = set()
    num_gerbils = len(males)

    for i in range(num_gerbils):

        male = males.pop()
        female = females.pop()
        pairs.add((male, female),)

    return pairs

print(mating_pairs({'Anne', 'Beatrice', 'Cari'}, {'Ali', 'Bob', 'Chen'}))