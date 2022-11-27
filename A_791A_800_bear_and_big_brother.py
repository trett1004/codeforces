# https://codeforces.com/problemset/problem/791/A
l = 0
b = 0
year_count = 0

x = input()
if len(x) == 5:
    l = 10
    b = 10
elif len(x) == 4:
    if x[1] != " ":
        l = 10
        b = int(x[3])
    else:
        l = int(x[0])
        b = 10
else:
    l = int(x[0])
    b = int(x[2])

while b >= l:
    l = l * 3
    b = b * 2
    year_count = year_count + 1
print(year_count)


