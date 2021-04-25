import matplotlib.pyplot as plt
import pandas as pd 

data = pd.read_csv('data.csv')

ages = data['Age']
all_devs = data['All_Devs']
python = data['Python']
javascript = data['JavaScript']

plt.plot(ages,python,label='Python')
plt.plot(ages,javascript,label = 'JavaScript')

plt.fill_between(ages,python,javascript, where=(python>javascript), 
                interpolate=True, alpha=0.25,label='Above JavaScript')

plt.fill_between(ages,python,javascript, where=(python<=javascript), 
                interpolate=True, color='r', alpha=0.25,label='Below JavaScript')
plt.legend()

plt.xlabel('Ages')
plt.ylabel('Salary')
plt.tight_layout()
plt.title('Python vs Javascript Salary')
plt.show()

