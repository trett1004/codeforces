# https://codeforces.com/problemset/problem/263/A

matrix = []

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

stepcounter = 0

for tc in range(5):
    line = input()
    # Make a Matrix
    row = []
    for j in range(len(line)):
        row.append(line[j])
    row.pop(1)
    row.pop(2)
    row.pop(3)
    row.pop(4)
    matrix.append(row)

#print(matrix[1][8])

newline = 5
# iterate through the lines to find the "1"
for i in range(5):
    for j in range(newline):
        if matrix[i][j] == "1":
            #Check how many fields the 1 had to move and print result
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
                '''
                if i == 0:
                    stepcounter = stepcounter + 5
                    stepcounter = newline - (j+1) + (3) + stepcounter
                    break
                elif i == 1:
                    stepcounter = newline - (j+1) + (3)
                    break
                elif i == 2 and j < 2:
                    stepcounter = 3 - (j+1)
                    break
                elif i == 2 and j == 2: # "1" is already in the middle
                    break
                elif i == 2 and j > 2:
                    stepcounter = (4 - (j+2))
                    break
                elif i == 3:
                    stepcounter = -(j) - (3)
                    break
                else:
                    stepcounter = stepcounter - 5 - j - 3
                    #stepcounter = -(newline) + (j+1) -(3) - stepcounter
                    break
                '''
            break

#print("newline:", newline)
#print("j+1:", j+1)
print(stepcounter)

#print("matrixij:", matrix[i][j])
#print("matrix2,4:", matrix[2][2])
#print("matrix1,8:", matrix[1][4])



    # for j in range(len(line)):
        #if line[j] == "1":
            
            
            
    # When "1" is found check for the position
    # When found the position move the "1" to the middle wich is line 3 / column 3 and set the old place to "0"



    
