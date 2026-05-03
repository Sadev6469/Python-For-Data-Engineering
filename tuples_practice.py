''' Data structures: Tuples'''
tuple = (101,22,13,41,5)
print(tuple) #Ordered List
tuple2 = (1,2,3,4,5,5)
print(tuple2) # Tuples Allows Duplicates
# tuple[0] = 5 #Tuple's are immutable , they wont allow item assignment - can't modify the tuple.
# print(tuple)
print(tuple[3]) # Tuples are indexed, elements can be accessed through index

print(sorted(tuple))


# Student Score Summary — Python Tuples Problem

## Problem Statement
'''Given a list of tuples containing student names and scores, write a program that:
1. Finds the **highest score**
2. Prints the **name(s) of students** who got that highest score
3. Calculates the **average score** of all students
4. Prints all students **sorted by score in descending order** with rank numbers
'''

students = [
    ("Alice", 85),
    ("Bob", 92),
    ("Charlie", 78),
    ("Diana", 92),
    ("Eve", 85),
    ("Frank", 70)
]
#Accessing every tuple in the list
for student in students:
    print(student)

#Getting the highest scores
scores = [student[1] for student in students]
new_scores = sorted(scores)
high_score = new_scores[-1] 
print('Max Score:',high_score)# high score 

#Accesing the student name of the top scorer
top_scorers = []
for student in students:
    if student[1] == high_score:
        top_scorers.append(student[0])
print(top_scorers)

#Average of the scores
avg_score = sum(new_scores) / len(new_scores)
print(avg_score)

#Ranking the students
sorted_scores = sorted(students, key=lambda student: student[1], reverse=True)
print(sorted_scores)
for index,student in enumerate(sorted_scores):
    print(f"{index+1}.{student[0]} - {student[1]}")
