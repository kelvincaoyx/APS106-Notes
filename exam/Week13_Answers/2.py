import random
import csv

# hardcoded data
assessments = ('Assignment1', 'Assignment2', 'Midterm1', 'Midterm2', 'Final')
num_parts = (1,2,4,5,5) # number of parts of each assessment
num_students = 30

with open("marks.csv", "w") as outfile:
    writer = csv.writer(outfile)
    
    for student in range(num_students):
        # Potential bug: may randomly produce same id more than once and so have 
        # multiple entries per student and assessment
        
        id = random.randint(100,1000)
        
        for i in range(len(assessments)):
            out_row = [id, assessments[i]]
            
            for p in range(num_parts[i]):
                out_row.append(str(random.randint(0,100/num_parts[i])))
                
            writer.writerow(out_row)
            
            