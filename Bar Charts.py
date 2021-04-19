from matplotlib import pyplot as plt
import pandas as pd
import numpy as np
#print(plt.style.available)
plt.style.use('fivethirtyeight')

ages_x = [18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31, 32, 33, 34, 35, 
36, 37, 38, 39, 40, 41, 42, 43, 44, 45, 46, 47, 48, 49, 50, 51, 52, 53, 54, 55]

py_dev_y = [20046, 17100, 20000, 24744, 30500, 37732, 41247, 45372, 48876, 53850, 57287, 63016, 65998, 70003, 70000, 71496, 75370, 83640, 84666,
 84392, 78254, 85000, 87038, 91991, 100000, 94796, 97962, 93302, 99240, 102736, 112285, 100771, 104708, 108423, 101407, 112542, 122870, 120000]

dev_y = [17784, 16500, 18012, 20628, 25206, 30252, 34368, 38496, 42000, 46752, 49320, 53200, 56000, 62316, 64928, 67317, 68748, 73752, 77232,
         78000, 78508, 79536, 82488, 88935, 90000, 90056, 95000, 90000, 91633, 91660, 98150, 98964, 100000, 98988, 100000, 108923, 105000, 103117]

# Set the x_indexes to be able to set the bars close to the oder by a margin of width
x_indexes = np.arange(len(ages_x))
width = 0.25

plt.bar(x_indexes,py_dev_y,label='Python Devs',width=width)
plt.bar(x_indexes+width,dev_y,linestyle='--',width=width,color = 'k',label='All Devs') #Color could be in hexa code #5a7d9a

plt.title('Median Salary (USD) by Age')

plt.xlabel('Ages')
plt.ylabel('Median Salary (USD)')

plt.tight_layout()
# Means where x_indexes are set xticks laberls equals to ages_x
plt.xticks(x_indexes,ages_x)

#plt.grid(True)

plt.legend()
plt.show()

