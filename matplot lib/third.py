from matplotlib import pyplot as plt
from collections import Counter
x_axis={"fail":0,"A1":0,"B":0,"A":0}
grades = [83,95,91,87,70,0,85,82,100,67,73,77,0]
for x in grades:
    if x>=80:
        x_axis["A1"]+=1
    elif x>=70:
        x_axis["A"] += 1
    elif x>=60:
        x_axis["B"] += 1
    else:
        x_axis["fail"] += 1
decile = lambda grade: grade // 10 * 10

histogram = Counter(decile(grade) for grade in grades)

plt.bar([x for x in x_axis.keys()], # shift each bar to the left by 4
        x_axis.values(), # give each bar its correct height
        8) # give each bar a width of 8
plt.axis([-5, 105, 0, 5]) # x-axis from -5 to 105,
 # y-axis from 0 to 5
plt.xticks([10 * i for i in range(11)]) # x-axis labels at 0, 10, ..., 100
plt.xlabel("Decile")
plt.ylabel("# of Students")
plt.title("Distribution of Exam 1 Grades")
plt.show()
