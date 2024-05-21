# Importing pandas and matplotlib
import pandas as pd
import matplotlib.pyplot as plt

netflix_df = pd.read_csv("netflix_data.csv")
netflix_subset = netflix_df[netflix_df['type'] == 'Movie']
netflix_movies = netflix_subset[["title", "country", "genre", "release_year", "duration"]]
short_movies = netflix_movies[netflix_movies.duration < 60]
colors = []
for lab, val in netflix_movies.iterrows():
    if val[2] == 'Children':
        colors.append('Green')
    elif val[2] == 'Documentaries':
        colors.append('Blue')
    elif val[2] == 'Stand-Up':
        colors.append('Red')
    else:
        colors.append('Yellow')
colors[:10]
fig = plt.figure(figsize=(12,8))
plt.scatter(netflix_movies['release_year'], netflix_movies['duration'], c = colors)
plt.xlabel('Release year')
plt.ylabel('Duration (min)')
plt.title('Movie Duration by Year of Release')
plt.show()
answer = "no"
