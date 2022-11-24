
n = input()
counter = 0

for i in n:
    if i == "7" or i == "4":
        counter = counter + 1
    else:
        pass

for i in str(counter):
    if i == "4" or i == "7":
        print("YES")
    else:
        print("NO")
        break





