import csv

def generate_student_marks(filename):
    '''
    (str) -> dictionary {id : {assessment : mark}}
    Opens the CSV file indicated by filename.
    Reads in the student mark records and stores them in a nested dictionary indexed
    first by ID and then by assessment name
    '''
    
    all_students = {}
    with open(filename, "r") as infile:
    
        reader = csv.reader(infile)
        for row in reader:
            id = row[0]
            assessment = row[1]
            total_mark = 0
            for mark in row[2:]:
                float_mark = float(mark)
                total_mark += float_mark
                    
            if id not in all_students:
                all_students[id] = {assessment : total_mark} 
            else:
                all_students[id][assessment] = total_mark
            
    return all_students

def calculate_average(all_students):
    '''
    (dict) -> list of tuples
    calculate the average mark for each students an return it in a list of tuples
    (id, average)
    '''
    mark_list = []
    for id in all_students:
        sum_mark = 0
        for assessment in all_students[id]:
            sum_mark += all_students[id][assessment]
        avg = sum_mark / len(all_students[id])
        mark_list.append((id, avg))
        
    return mark_list

students = generate_student_marks("marks.csv")
print(students, len(students))

student_list = calculate_average(students)
print(student_list)

