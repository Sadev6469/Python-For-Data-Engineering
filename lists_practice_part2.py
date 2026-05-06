'''All about lists'''

#Adding elements into a list
char = ['a','b','c','d','e']
#add the element to the end of the list
char.append('f')
print(char)

#Adding a list to the end of a nested list
matrix = [['a','b','c'],
          ['d','e','f']]
matrix.append(['g','h','i'])
print(matrix)
matrix.insert(0,['s','s','s'])
print(matrix)

#Adding an item to a specific row in a list
mat = [['a','b','c'],
          ['d','e','f']]
mat[1].append('x')
mat[0].insert(0,'z')
print(mat)


#insert elmenent at a specific position
char.insert(2,'sowjanya')
print(char)


#Removing Items from a list

#Remove everything from a list
chars = ['a','b','c','d','e']
chars.clear()
print(chars) #returns an empty list
chars = ['a','b','c','d','e']
#Removing last item in a list
chars.pop()
print(chars)
#Removing element from a specific position
chars.remove('b') #pass the specific element you want to remove
print(chars)

#Removing items from a nested list
m = [['a','b','c'],
          ['d','e','f'],
          ['g','h','i']]
#Remove by value
m.remove(['a','b','c'])
print(m)
#Remove by index
m.pop(0)
print(m)
#Remove element from a specific row
mx= [['a','b','c'],
          ['d','e','f'],
          ['g','h','i']] #remove g from this nested matrix
#mx[2].remove('g') or
mx[2].pop(0)
print(mx)
scores = [100,98,45,64,99,85,92]
high_scores = [score for score in scores if score > 90]
print(high_scores)

#updating a list
values = ['a','b','c','d','e']
values[0] = 'Sowji'
print(values)

mat = [['a','b','c'],
          ['d','e','f'],
          ['g','h','i']]
mat[-1][-1] = 'k'
print(mat)

#Sorting Lists
marks = [23,54,87,34,29,89,98]
marks.sort() #default sort - ascending order
marks.sort(reverse= True) #descending order
print(marks)

#Sorting a nested list
matrix1 = [['g','h','i'],
          ['d','e','f'],
          ['a','b','c']]
matrix1.sort()
matrix1.sort(reverse=True)
print(matrix1)

#sorting without changing the contents of an original list.
marks = [23,54,87,34,29,89,98]
sorted_marks = sorted(marks) #This will return a list
print(sorted_marks)

#Reversing a list
marks = [23,54,87,34,29,89,98]
marks.reverse()
print(marks)

#Reverse without changing the contents of a list
marks = [23,54,87,34,29,89,98]
reversed_marks = reversed(marks)
reversed_marks = list(reversed(marks)) # This returns an Iterator object
print(reversed_marks)

#copying lists
#Method1-using '=' operator
list1 = ['shampoo','conditioner','comb','serum']
list2 = list1
print(list1)
print(list2)
list2[2] = 'hair comb'
list2.pop() #impacts original list as well because of pointing to the original list
print(list1,list2)

#Method2 - list.copy()
list1 = ['shampoo','conditioner','comb','serum']
list2 = list1.copy() #This creates a copy of the original list but they point to diffrent memory addresses
print(list1,list2)
list2.append('coconut oil') #Changes on copied list wont imapct on the original list
print(list1,list2) 

#Method3 - deepcopy()
import copy #copy is not part of built-in modules
list1 = ['dryer','steamer','iron box','heater']
list2 = copy.deepcopy(list1)
list2.append('washer') #won't impact original list
print(list1)
print(list2)

#combining lists

#Method 1
high_scores = [100,98.95,93,96,99]
loww_scores = [89,78,65,79,84,80,45]
scores = high_scores + loww_scores
print(scores) # combines all the items from both the list into a single list.

#Method 2 
#if you the wnat lists to be in the form of individual lists - nested lists inside a list.
high_scores = [100,98.95,93,96,99]
low_scores = [89,78,65,79,84,80,45]
scores = [high_scores,low_scores]
print(scores)

#Method 3 using list.extend() method
high_scores = [100,98.95,93,96,99]
low_scores = [89,78,65,79,84,80,45]
high_scores.extend(low_scores)
print(high_scores) #only extending lists gets updated.
print(low_scores) #the second list doesnt change.

#Method 4 using zip() function
names= ['sow','suj','gow','tat','vish','andal']
scores = [89,78,65,79,84,80]
list = list(zip(names,low_scores)) #zip returns an iterator object.
print(list)






