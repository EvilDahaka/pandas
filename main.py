import pandas as pd
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


