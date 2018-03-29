# File: Lists_in_Python_as_two-dimensional_arrays.py
# Description: Examples how to create 2-dimensional lists in Python and use them as arrays
# Environment: PyCharm and Anaconda environment
#
# MIT License
# Copyright (c) 2018 Valentyn N Sichkar
# github.com/sichkar-valentyn
#
# Reference to:
# [1] Valentyn N Sichkar. Lists in Python as two-dimensional arrays // GitHub platform [Electronic resource]. URL: https://github.com/sichkar-valentyn/Lists_in_Python_as_two-dimensional_arrays (date of access: XX.XX.XXXX)

m = 'end'
a = []
b = []
# Creating 2-dimensional list (initial list)
while m not in a:
    a = [i for i in input().split()]  # Creating one dimensional list of string values
    b += [a]  # Creating two dimensional list of lists values

del b[len(b) - 1]  # Deleting the last list of the 2-dimensional list which is ['end']

# Creating empty list with the same dimensions as in list b (initial list)
c = []
for i in range(len(b)):
    c += [[0 for j in range(len(b[i]))]]
print(c)  # Checking that 2-dimensional list is created correctly

# Changing the values inside the 2-dimensional lists from string to integer
for i in range(len(b)):
    for j in range(len(b[i])):
        b[i][j] = int(b[i][j])
        c[i][j] = b[i][j] # Assigning the same values to list c as in list b


# Implementing the task - changing the current cell as a sum of surrounded by neighbours cells
# c[i][j] = c[i-1][j] + c[i+1][j] + c[i][j-1] + c[i][j+1]
# For the border cells the neighbours are the cells on the opposite side of the array
# In some cases the neighbours can be the initial cell intself
sum = 0
for i in range(len(b)):
    for j in range(len(b[i])):
        if i - 1 < 0:
            sum += c[-1][j]
        else:
            sum += c[i - 1][j]
        
        if i + 1 > len(b) - 1:
            sum += c[0][j]
        else:
            sum += c[i + 1][j]
        
        if j - 1 < 0:
            sum += c[i][-1]
        else:
            sum += c[i][j - 1]
        
        if j + 1 > len(b[i]) - 1:
            sum += c[i][0]
        else:
            sum += c[i][j + 1]
        
        b[i][j] = sum
        sum = 0

print(c)  # Showing the initial 2-dimensional list
print(b)  # Showing the changed 2-dimentional list

# Showing the result in form of array
for i in range(len(b)):
    if i != 0 or i != len(b) - 1:
        print()
    for j in range(len(b[i])):
        print(b[i][j], end=' ')
