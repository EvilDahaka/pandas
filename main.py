import pandas as pd
import matplotlib.pyplot as plt
df = pd.read_csv('IMDB-Movie-Data.csv')
print('___________')
print(df.info())

#Чи впливає рік випуску фільму на його рейтинг?
data_cleaned = df[['Year', 'Rating']].dropna()

average_rating_by_year = data_cleaned.groupby('Year')['Rating'].mean()

print("Середній рейтинг фільмів за роками:")
print(average_rating_by_year)

#Чи змінюється середній рейтинг фільмів залежно від жанру?
data_cleaned = df[['Rating', 'Genre']].dropna()

average_rating_by_genre = data_cleaned.groupby('Genre')['Rating'].mean().sort_values(ascending=False)

print("Середній рейтинг фільмів за жанрами:")
print(average_rating_by_genre)

# df['Rank'].value_counts().plot(kind = 'pie')
# plt.show()

#df.plot(x = 'Rating',
        #y = 'Year',
        #kind = 'scatter')

#plt.show()

df['Genre'].value_counts().plot(kind = 'pie')
plt.show()

df['Rank'].value_counts().plot(kind = 'bar')
plt.show()


        




