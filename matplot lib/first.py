#chart is a graphical representation of numerical data
from matplotlib import pyplot as plt
lis1=[x for x in range(1,21)]

lis2=[y*5 for y in lis1]

print(lis2)

plt.plot(lis1, lis2, color='green', marker='0', linestyle='solid')

# add a title
plt.title("kuch bhi")
# add a label to the y-axis
plt.ylabel('multiple of 5')
plt.show()