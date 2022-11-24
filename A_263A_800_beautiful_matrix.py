# https://codeforces.com/problemset/problem/263/A

matrix = []
row = []
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
newline = 5
#print(matrix[1][8])
# iterate through the lines to find the "1"
for i in range(5):
    for j in range(newline):
        if matrix[i][j] == "1":
            if matrix[i][j] == matrix[2][3]:
                i = 4
                j = 4
                #print("0")
                break
            else:
                # Set "1" in the middle of the matrix (matrix[2][4]) and change original field of "1" to "0"
                matrix[2][3] = "1"
                matrix[i][j] = "0"
                #Check how many fields the 1 had to move and print result

                for p in range(i):
                    if i == 0:
                        stepcounter = stepcounter + 4
                        stepcounter = newline - (j+1) + (3) + stepcounter
                        break
                    elif i == 1:
                        stepcounter = newline - (j+1) + (3)
                        break
                    elif i == 2 and j < 2:
                        stepcounter = 3 - (j+1)
                        break
                    elif i == 2 and j == 2:
                        break
                    elif i == 2 and j > 2:
                        stepcounter = (j+1) - (3-j)
                        break
                    elif i == 3:
                        stepcounter = -newline + (j+1) -(3)
                        break
                    else:
                        stepcounter = stepcounter - 4
                        stepcounter = -(newline) + (j+1) -(3) - stepcounter
                        break
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



    
