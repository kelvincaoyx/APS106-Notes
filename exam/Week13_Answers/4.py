import csv

class Student:
    '''An object that represents student information'''
    
    def __init__(self, id):
        '''
        (self,str) -> NoneType
        Assigns the id, creates an empty marks dictionary
        '''
        self.id = id
        self.marks = {}
        
    def __str__(self):
        '''
        (self) -> str
        '''
        ret_str = self.id + " ["
        for assessment in self.marks:
            ret_str += "(" + assessment + "," + str(self.marks[assessment]) + ")"
        ret_str += "]"
        return ret_str

    def add_mark(self, assessment, mark):
        '''
        (self, str, num) -> NoneType
        Adds num as the mark for assessment
        '''
        self.marks[assessment] = mark  # overwrites existing mark if any. Check?

    def calc_avg(self):
        '''
        (self) -> float
        Returns the average mark over the assessments
        '''
        total_mark = 0
        for assessment in self.marks:
            total_mark += self.marks[assessment]
        return total_mark / len(self.marks)

def generate_student_marks(filename):
    '''
    (str) -> dictionary {str : Student}
    Parse the student data from CSV file filename
    '''
    
    all_students = {}
    with open(filename, "r") as infile:
    
        reader = csv.reader(infile)
        for row in reader:
            id = row[0]
            if id not in all_students:
                s = Student(id)
                all_students[id] = s
            else:
                s = all_students[id]
                
            assessment = row[1]
            total_mark = 0
            for mark in row[2:]:
                float_mark = float(mark)
                total_mark += float_mark
                
            s.add_mark(assessment, total_mark)
                        
    return all_students

def calculate_average(all_students):
    '''
    (dict of Students) -> list of tuples
    calculate the average mark for each students an return it in a list of tuples
    (id, average)
    '''
    mark_list = []
    for id in all_students:
        mark_list.append((id, all_students[id].calc_avg()))
        
    return mark_list

students = generate_student_marks("marks.csv")
for s in students:
    print(students[s])
    
student_list = calculate_average(students)
print(student_list)