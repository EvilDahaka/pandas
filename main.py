import pandas as pd
import matplotlib.pyplot as plt
df = pd.read_csv('IMDB-Movie-Data.csv')
print('___________')
print(df.info())

print(df.columns)

#Чи впливає рік випуску фільму на його рейтинг?

# Очистка даних: залишаємо лише колонки "Year" і "Rating", прибираємо пропущені значення
data_cleaned = df[['Year', 'Rating']].dropna()

# Обчислення середніх рейтингів за роками
average_rating_by_year = data_cleaned.groupby('Year')['Rating'].mean()

# Виведення середнього рейтингу за роками
print("Середній рейтинг фільмів за роками:")
print(average_rating_by_year)

# Перевірка відмінностей між середніми рейтингами
min_rating = average_rating_by_year.min()
max_rating = average_rating_by_year.max()

# Логіка для відповіді
if max_rating - min_rating > 0.5:  # Задаємо поріг значущої різниці
    print("\nТак")  # Рік впливає на рейтинг
else:
    print("\nНі")  # Рік не впливає на рейтинг


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

#df['Genre'].value_counts().plot(kind = 'pie')
#plt.show()

#df['Rank'].value_counts().plot(kind = 'bar')
#plt.show()

plt.figure(figsize=(10, 6))
df.groupby('Year')['Rating'].mean().plot(kind='line', color='blue')
plt.title('Середній рейтинг фільмів за роками')
plt.xlabel('Рік')
plt.ylabel('Середній рейтинг')
plt.grid(True)
plt.show()

# Стовпчаста діаграма: 10 фільмів з найвищим рейтингом
top_10_movies = df.nlargest(10, 'Rating')
plt.figure(figsize=(10, 6))
top_10_movies.plot(x='Title', y='Rating', kind='bar', color='green')
plt.title('10 фільмів з найвищим рейтингом')
plt.xlabel('Назва фільму')
plt.ylabel('Рейтинг')
plt.xticks(rotation=90)
plt.show()

# Кругова діаграма: розподіл фільмів за жанрами
genre_counts = df['Genre'].str.split(',').explode().value_counts()
plt.figure(figsize=(8, 8))
genre_counts.plot(kind='pie', autopct='%1.1f%%', startangle=90, cmap='tab20')
plt.title('Розподіл фільмів за жанрами')
plt.ylabel('')
plt.show()

# Гістограма: розподіл рейтингів
plt.figure(figsize=(10, 6))
df['Rating'].plot(kind='hist', bins=20, color='purple', edgecolor='black')
plt.title('Розподіл рейтингів фільмів')
plt.xlabel('Рейтинг')
plt.ylabel('Частота')
plt.show()

# Діаграма розсіювання: рейтинг проти доходу
plt.figure(figsize=(10, 6))
df.plot(kind='scatter', x='Revenue (Millions)', y='Rating', color='red')
plt.title('Рейтинг проти доходу фільмів')
plt.xlabel('Доходи (Revenue in Millions)')
plt.ylabel('Рейтинг')
plt.show()


        




