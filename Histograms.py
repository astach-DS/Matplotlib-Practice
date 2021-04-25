import matplotlib.pyplot as plt
import pandas as pd 

data = pd.read_csv('data.csv')
bins=[10,20,30,40,50,60,70,80,90,100]
ages = data['Age']

plt.hist(ages,bins=bins,edgecolor='k')
plt.axvline(ages.median(),color='r',linestyle='--',label='Median Age')

plt.xlabel('Ages')
plt.ylabel('Total Respondents')
plt.title('Age of Respondents')

plt.legend()
plt.show()