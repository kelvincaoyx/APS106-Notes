# Create a list of students and grades in all their courses using nested lists
#
# Write a function that takes the database and a grade as arguments and 
# returns a list of the students who got that grade in any course.

marks = [["Mohamed", ["A", "A+", "C", "FZ", "B-"]],
         ["Cindy", ["B", "B", "C", "A", "B"]],
         ["Mustafa", ["A", "A+", "A+", "C", "C"]],
         ["Stefan", ["FZ", "B", "B", "C", "C"]]]

def find_students_with_grade(all_marks, grade):
    ''' (list, str) -> list
    Returns a list of students who received a mark equal to grade 
    in any course.
    '''
    students_with_grade = []
    for record in all_marks:
        if grade in record[1]:
            students_with_grade.append(record[0])
    
    return students_with_grade

# The 'in' operator in the if-statement above is particularly useful here.
# Many computer lanaguages cannot do this however and so you need to
# loop over each element of the marks list explicitly. Here's a way to do
# it without the in-operator in the if-statement
def find_students_with_grade_nested(all_marks, grade):
    ''' (list, str) -> list
    Returns a list of students who received a mark equal to grade 
    in any course.
    '''
    students_with_grade = []
    for record in all_marks:
        name = record[0]
        for mark in record[1]:
            if mark == grade and name not in students_with_grade:    
                students_with_grade.append(record[0])
    
    return students_with_grade

# The implementation above is a bit unsatisfactory since even after we've
# identified a student to be added to the list, we keep looping through
# his/her other marks. Why not just stop the 'for mark in record[1]' loop
# as soon as we find a matching mark?
#
# Here are two ways to do this.

def find_students_with_grade_break(all_marks, grade):
    ''' (list, str) -> list
    Returns a list of students who received a mark equal to grade 
    in any course.
    '''
    students_with_grade = []
    for record in all_marks:
        name = record[0]
        for mark in record[1]:
            if mark == grade:    
                students_with_grade.append(record[0])
                break     # jump out of the inner-most loop
            
    return students_with_grade

# Some programmers (like Prof Beck) don't like break because it "jumps out"
# of a loop and so the flow of the program is less structured and (slightly)
# worse. In this case, however, using break (as above) probably leads to 
# simpler code. 

# Here is a way to do it without break - using a while loop 
def find_students_with_grade_while(all_marks, grade):
    ''' (list, str) -> list
    Returns a list of students who received a mark equal to grade 
    in any course.
    '''
    students_with_grade = []
    for record in all_marks:
        name = record[0]
        i = 0
        student_found = False
        while not student_found and i < len(record[1]):
            if record[1][i] == grade:    
                students_with_grade.append(record[0])
                student_found = True
            i += 1
            
    return students_with_grade


if __name__ == '__main__':
    print(find_students_with_grade(marks, "A+"))
    print(find_students_with_grade(marks, "A"))
    print(find_students_with_grade(marks, "FZ"))
    
    print("")           
    print(find_students_with_grade_nested(marks, "A+"))
    print(find_students_with_grade_nested(marks, "A"))
    print(find_students_with_grade_nested(marks, "FZ"))

    print("")           
    print(find_students_with_grade_break(marks, "A+"))
    print(find_students_with_grade_break(marks, "A"))
    print(find_students_with_grade_break(marks, "FZ"))

    print("")
    print(find_students_with_grade_while(marks, "A+"))
    print(find_students_with_grade_while(marks, "A"))
    print(find_students_with_grade_while(marks, "FZ"))
