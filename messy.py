
# Original code with unclear names and repeated logic

import math

marks = [65, 80, 45, 90, 70]
total = 0

for m in marks:
    total = total + m

average = total / len(marks)
print("Marks:", marks)
print("Class average:", average)

def f(x):
    s = 0
    for i in x:
        s = s + i
    return s / len(x)

print("Average again:", f(marks))
