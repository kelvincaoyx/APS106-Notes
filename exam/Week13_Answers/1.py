
def swap_lines_list(filename):
    '''
    (str) -> NoneType
    Creates a new file containin the lines of filename with consecutive
    lines swapped
    '''
    
    with open(filename, "r") as infile:
    
        file_lines = []
        for line in infile:
            file_lines += [line.strip()]

    swapped_lines = []
    for i in range(0,len(file_lines),2):
        if i+1 < len(file_lines):
            swapped_lines.append(file_lines[i+1])
        swapped_lines.append(file_lines[i])
    
    # create name of new file. Only works with standard names - one "."
    name_parts = filename.split(".")
    out_name = name_parts[0] + "_rev." + name_parts[1]

    with open(out_name, "w") as outfile:
        for line in swapped_lines:
            outfile.write(line + "\n")


def swap_lines_nolist(filename):
    '''
    (str) -> NoneType
    Creates a new file containin the lines of filename with consecutive
    lines swapped
    '''
    
    # create name of new file. Only works with standard names - one "."
    name_parts = filename.split(".")
    out_name = name_parts[0] + "_nolist_rev." + name_parts[1]
    
    with open(filename, "r") as infile, open(out_name, "w") as outfile:
        
        line1 = infile.readline()
        while line1 != "":             # while still a real line
            line2 = infile.readline()
            if line2 != "":            # line2 is also a real line
                outfile.write(line2)
            outfile.write(line1)
            line1 = infile.readline()
            
# swap_lines_list("lyrics.txt")
# swap_lines_nolist("lyrics.txt")

import random
class Grades:
    def __init__(self):
        self.id = random.randint(100,999)
        self.Assignment1 = [random.randint(0,100)]
        self.Assignment2 = [random.randint(0,100),random.randint(0,100)]
        self.Midterm1 = [random.randint(0,100),random.randint(0,100),random.randint(0,100),random.randint(0,100)]
        self.Midterm2 = [random.randint(0,100),random.randint(0,100),random.randint(0,100),random.randint(0,100),random.randint(0,100)]
        self.Final = [random.randint(0,100),random.randint(0,100),random.randint(0,100),random.randint(0,100),random.randint(0,100)]
        

testGrade = Grades()

file = () 

    