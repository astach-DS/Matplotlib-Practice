import pandas as pd
import matplotlib.pyplot as plt
from collections import Counter

data = pd.read_csv('data.csv')

# Split the languages by ';' then they are added to languages_list
languages_list=[]
for i in range(data.shape[0]):
    language_split = data['LanguagesWorkedWith'][i].split(';')
    for i in language_split:
        languages_list.append(i)
#Count method counts the times a language apear
languages_list_count = Counter(languages_list)
#Returns a lists of tuple with top 15 languages
top_15_languages = languages_list_count.most_common(15)

languages=[]
popularity=[]

# For each tuple in the list, it creates 2 list, one with the element 0 of the tuple
#which is the language and second, the popularity of it which is the last element of the tuple
for i in top_15_languages:
    languages.append(i[0]) 
    popularity.append(i[1])
# Reverse the order of the lists
languages=languages[::-1]
popularity=popularity[::-1]

plt.barh(languages,popularity)
plt.tight_layout()
plt.title('Top 15 Languages')
plt.xlabel('Popularity')
plt.show()

###### Other way to do the same #######

#data=pd.Series(languages_list)

#data = data.value_counts()
#languages = list(data.index)
#languages_count = list(data.values)

#languages.reverse()

#languages_count.reverse()