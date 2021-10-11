import numpy as np
import random

#2-D array because rows and columns
    # 2 rows and 3 columns: (123) is first row, (456) is second row
arr01 = np.array([[1,2,3],[4,5,6]])

#1-D array because just one row
arr02 = np.array([0.0,0.1,0.2,0.3,0.4])

for row in arr01:
    print(row)
    for column in row:
        print(column,end=' ')
    print()



#flat removes all row and column elements, just prints every value
for i in arr01.flat:
    print(i)

arr03 = np.zeros(5)

arr04 = np.ones((2,4), dtype=int)

arr05 = np.full((3,5), 13)


#EXERCISE----------------------------------
#create a 2 dimensional array of 5 integer elements using the
#random module and list comprehension

a = np.array([[random.randint(1,10) for i in range(5)],
            [random.randint(1,10) for x in range(5)]])

b = np.array(np.random.randint(1,10,size=(2,5)))

arr06 = np.arange(5)

arr07 = np.arange(5,10)

arr08 = np.arange(10,1,-2)

#linspace() allows you to create an array of numbers that are equally spaced out between 
#the two numbers given
arr09 = np.linspace(0.0,1.0,num=5)

#reshape must be a factor/multiple of the number
arr10 = np.arange(1,21).reshape(4,5)


num01 = np.arange(1,6)

num02 = num01*2

num03 = num01**3
#this is called broadcasting, take  all the elements in an array
#and multiple it by the oeprator

num04 = num01 * num02
#these arrays ^^ have to be the same size- multiples all the elements
# in array 1 by the elements in array 2

num05 = num01> 13

num06 = num03 > num01
#gives a boolean if the elements in num03 are greater than the elements
#in num01



#Here we have an array of 4 students grades on 3 exams
#row = student
#column = exam
grades = np.array([[87,96,70],[100,87,90],[94,77,90],[100,81,82]])

print(grades.sum())
print(grades.mean())
print(grades.std())
print(grades.var())


#if wanted to find the average grades for each exam
grades_by_exam = grades.mean(axis=0) #gives a 1-d array with 3 elements (for each exam)
#axis=0   --  calculate average on all rows for each column

#if watned to find the average on all exams for each student
grades_by_student = grades.mean(axis=1) #gives a 1-d array with 4 elements (for each student)
#axis=1  --  calculate average on all columns for each row


num07 = np.array([1,4,9,16,25,36])
num08 = np.sqrt(num07)

num09 = np.array([10,20,30,40,50,60])
num10 = np.add(num07,num09)
#same as
num10 = num07 + num09

num11 = np.multiply(num09,5)
#same as
num11 = num09 * 5
#another example of broadcasting- multiple by the number of elements that are in the array

num12 = num09.reshape(2,3)
#2 rows of 3 columns
num13 = ([2,4,6])
num14 = np.multiply(num12,num13)
#**** number of rows don't have to matchup, but the number of columns do
#**** so each row was multipied by 2, 4, and 6






print()