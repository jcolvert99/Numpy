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

arro8 = np.arange(10,1,-2)


print()