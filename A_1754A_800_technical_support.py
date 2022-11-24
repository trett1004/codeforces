# https://codeforces.com/problemset/problem/1754/A?f0a28=1
# Problemset 1754A

y = "Yes"
n = "No"
q_counter = 0
a_counter = 0

# Get input
t = int(input())
for tc in range(t):
    m = int(input())
    qastring = input()
    q_counter = qastring.count("Q")
    a_counter = qastring.count("A")

    #Start code
    if qastring[-1] == "Q":
        print(n)
        continue

    # If there are less A than Q looking from the the end e.g. check last 3 chars: QAAAQQA
    a_counter_reverse = 0
    letters = 0
    for c in reversed(qastring):
        letters = letters + 1
        if c == "A":
            a_counter_reverse = a_counter_reverse + 1

        if letters - a_counter_reverse > a_counter_reverse:
            print(n)
            break

    if letters - a_counter_reverse > a_counter_reverse:
        continue
    if q_counter > a_counter:
        print(n)
    else:
        print(y)


