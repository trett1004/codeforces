# https://codeforces.com/problemset/problem/263/A

matrix = []

# Following commenting  used for Testingpurpuses
'''
row1 = ['0', '0', '0', '0', '0']
row2 = ['0', '0', '0', '0', '0']
row3 = ['0', '0', '0', '0', '0']
row4 = ['0', '0', '0', '0', '0']
row5 = ['0', '0', '0', '0', '1']


matrix.append(row1)
matrix.append(row2)
matrix.append(row3)
matrix.append(row4)
matrix.append(row5)
'''
# Variable that contains the answer in the end
stepcounter = 0

# Get input
for tc in range(5):
    line = input()
    # Make a Matrix
    row = []
    for j in range(len(line)):
        row.append(line[j])
    # Remove empty spaces in the matrix
    row.pop(1)
    row.pop(2)
    row.pop(3)
    row.pop(4)
    matrix.append(row)

# Reduced linelength from 9 to 5 because of row.pop above
newline = 5
# iterate through the lines to find the "1"
for i in range(5):
    for j in range(newline):
        if matrix[i][j] == "1":
            #Check how many fields the 1 had to move to the middle and print result
            for p in range(i+1):
                if i == 0 or i == 4:
                    stepcounter = stepcounter + 2
                elif i == 1 or i == 3:
                    stepcounter = stepcounter + 1
                if j == 0 or j == 4:
                    stepcounter = stepcounter + 2
                elif j == 1 or j == 3:
                    stepcounter = stepcounter + 1
                else:
                    stepcounter = stepcounter + 0
                break
            break
print(stepcounter)





    
