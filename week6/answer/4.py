
def count_vowels_count(s):
    '''
    (str) -> NoneType
    Print a table of the count of the number of times each vowel appears in s
    '''
    print("Vowel\tOccurences")
    vowels = "aeiou"
    s = s.lower()
    
    for v in vowels:
        v_count = s.count(v)
        print(v,"\t",v_count)

def count_vowels_no_count(s):
    '''
    (str) -> NoneType
    Print a table of the count of the number of times each vowel appears in s
    '''
    print("Vowel\tOccurences")
    vowels = "aeiou"
    s = s.lower()
    
    for v in vowels:
        v_count = 0
        for ch in s:
            v_count += (ch == v)
            
        print(v,"\t",v_count)

count_vowels_count("This is the time that all good children are aslEEp.")
count_vowels_no_count("This is the time that all good children are aslEEp.")