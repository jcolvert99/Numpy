import numpy as np

#ROWS - students / COLUMNS - each test
grades = np.array([[87,96,70],[100,87,90],[94,77,90],[100,81,82]])


#give you all the grades for student 1: [100,87,90]
student1 = grades[1]

# "row , column"
student0_test1 = grades[0,1]

# ":" represents sequential values and the upper bound is not including
# shows the grades for student 0 and 1 -- SPLICING for 2 rows
students0_1 = grades[0:2]

#non-sequential rows- double brackets only represents the row part, not the column part
#gives all the grades for students 1 and 3
students1_3 = grades[[1,3]]

#gives only test 2 for students 1 and 3
#each inner bracket respresents specific rows and columns
students1and3_test2 = grades[[1,3],[2]]
# grades[[rows][columns]]

# just ":" gives you all rows
allstudents_test0 = grades[:,0]

#don't need brackets if you're doing consecutive rows, only need it with a comma
allstudents_test1and2 = grades[:,1:3]

alstudents_test0and2 = grades[:,[0,2]]

'''
use Numpy random-number generation to create an array of 12 random grades in the range 60 to 100,
then reshape the results into a 3-by-4 array. Calculate the average of all the grades, the average of the students
grades for each test and the averages of the grades for each student
'''

grades = np.random.randint(60,101,12).reshape(3,4)  #12 numbers between 60 and 100
grades.mean()
grades.mean(axis=0) #axis=0  -- aggregate value at bottom
grades.mean(axis=1) #axis=1  -- aggregate value at far right



#SHALLOW COPIES - change to the original affects the shallow copy
numbers = np.arange(1,6)
numbers_view = numbers.view() #view method creates a shallow copy

numbers[1] *= 10

numbers_view[1] /= 10

numbers_slice = numbers[0:3]

numbers[1] *= 20



#DEEP COPIES - change to the original does NOT affect the deep copy
numbers_copy = numbers.copy() #copy method creates a deep copy

numbers[1] *= 10


grades = np.array([[87,96,100],[100,87,90]])
grades_reshaped = grades.reshape(1,6)
#reshape method produces a shallow copy

grades.resize(1,6)


flattened = grades.flatten()
#flatten creates a deep copy


raveled = grades.ravel()
#ravel creates a shallow copy
raveled[0] = 100
flattened[1] = 100


grades = np.array([[87,96,100],[100,87,90]])
grades.T #transpose- flips the rows and columns
grades2 = np.array([[94,77,90],[100,81,82]])

#hstack adds more rows
h_grades = np.hstack((grades,grades2))

#vstack adds more columns
v_grades = np.vstack((grades,grades2))















print()