import matplotlib.pyplot as plt

slices = [59219, 55466, 47544, 36443, 35917]
labels = ['JavaScript', 'HTML/CSS', 'SQL', 'Python', 'Java']
explode = [0,0,0,0.1,0]
plt.pie(slices,labels=labels,wedgeprops={'edgecolor':'black'},
         explode=explode,autopct='%1.1f%%',shadow=True)
plt.title('My Pie Chart')
plt.show()