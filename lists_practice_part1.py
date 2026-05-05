'''All about Lists'''
'''How to create Lists'''
#.Creating an empty list 
empty = []
print(type(list))

#Creating a list from a string
name = 'sowjanya'
print(list(name))

#Creating a list from range function
numbers = list(range(10))
print(numbers)

#Creating a nested list in python
matrix = [['a','b','c'],
          ['d','e','f']]
print(matrix)
print(matrix[0]) #Accessing only first row
print(matrix[0][0]) # Accesing the first element in the  row.
print(matrix[1][2]) # Accesing the last element in the last row.
print(matrix[-1][-1]) #Accesing the last element in the last row

student_scores = [('sowji',100),
                  ('Sammu',99),
                  ('Anwitha',95)]
print(student_scores[0]) # Accesing the first elemnt in the list
print(student_scores[0][1]) # Accesing only the first student scores.
for student in student_scores:
    print(student[1])
scores = [student[1] for student in student_scores]
print(scores)


#Slicing a single list 
char = ['a','b','c','d','e']
print(char[0:2]) # accessing first two elemnets of a list 
print(char[:2]) # accessing first two elements of a list
print(char[:]) # accessing the whole list 
print(char[1:]) # accessing the elemnts from first index to last index

#slicing a nested list
mat = [['a','b','c'],
          ['d','e','f'],
          ['g','h','i']]
print(mat[0:2]) # accesing first 2 rows in a list 
print(mat[:]) # accessing the whole rows in the list
print(mat[1:]) #accessing the last 2 rows in a list
print(mat[2][:2]) # accesing only first 2 elemnts in the last row

#Unpacking in Lists
person = ['sowjanya','25','Atlanta','Georgia','Data engineer']
name, age, city, state, job_title = person
print(name)
print(job_title)

bio_data = ['sowjanya','25','Atlanta','Georgia','Data engineer']
name, *details, job_title = bio_data
print(name)
print(*details) #collects all the remaining items in to a new list during unpacking.

#Real-time use case
path = "year=2024/month=01/day=15"
for segment in path.split("/"):
    key, value = segment.split("=")   # unpacking a 2-item list
    print(key, value)

bio_data = ['sowjanya','25','Atlanta']
name, age, city , *details = bio_data
print(age)
print(*details)

person = ['Sowji','Atlanta','DE','26']
name, *_ = person
print(name)
print(_)

#Exploring and Analysing Lists

#Analyzing 
scores = [89,100,34,87,98]
print('maximum score:',max(scores))
print('minimum score:',min(scores))
print('Total score:',sum(scores))
print('Length of the list:',len(scores))

#Completeness and existence check
scores = [35,100,34,87,0]
print(any(scores)) #True if atleast one of the element in the list has a real value
print(all(scores)) #Only True if all the elements in the list has a real value

#Practice problem
# [month, region, revenue, units_sold, returns]
sales_records = [
    ["Jan", "North", 84500, 320, 12],
    ["Jan", "South", 62300, 215,  8],
    ["Jan", "East",  91200, 410, 19],
    ["Feb", "North", 78900, 298, 15],
    ["Feb", "South", 55100, 189,  5],
    ["Feb", "East",  102400, 467, 22],
    ["Mar", "North", 93000, 355, 10],
    ["Mar", "South", 71800, 260, 14],
    ["Mar", "East",  88600, 390, 17],
]

#To check if any high returns detected for a month
if any(row[4] > 20 for row in sales_records):
    print("high returns detected")
#To check if all the months reached its 50k revenue target
if all(row[2] > 50000 for row in sales_records):
    print("All regions meeting revenue threshold")

#To check if all the regions sold 100+ units and atleast one region crossed 100k revenue
if all(row[3] > 100 for row in sales_records) and any(row[2] > 100000 for row in sales_records):
    print("All regions sold 100+ units and at least one region crossed 100k revenue")

#Count the occrences of an item in a list
scores = [35,100,34,87,0,100,100]
print(scores.count(100))

#Find the position of an item in a list
scores = [35,100,34,87,0,100,100]
print(scores.index(100))

#Membership and Identity

#Checks if an item exists in a list
scores = [35,100,34,87,0,100,100]
print(34 in scores)

#check if two lists are identical
list1 = ['allam','sowji','data-engineer', 'has experience']
list2 = ['allam','sowji','data-engineer', 'has experience']
print(list1 == list2)
