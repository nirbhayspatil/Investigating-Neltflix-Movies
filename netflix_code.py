# -*- coding: utf-8 -*-
"""
Created on Fri Mar 29 12:23:33 2024

@author: PatilNi
"""

# Importing pandas and matplotlib
import pandas as pd
import matplotlib.pyplot as plt


# Loading the data
netflix_df = pd.read_csv('netflix_data.csv')
netflix_df.head()

# Creating subset for 'Movies' only
netflix_subset = netflix_df[netflix_df['type']!='TV Show']

# Selecting required columns from data
col = ['title', 'country', 'genre', 'release_year', 'duration']
netflix_movies = netflix_subset[col]

# Filter the data for movies less than 60 minutes of duration
short_movies = netflix_movies[netflix_movies['duration'] < 60]
short_movies.head(20)

# Define empty list
colors = []

for genre in netflix_movies['genre']:
    if genre == "Children":
        colors.append("blue")  
    elif genre == "Documentaries":
        colors.append("green")
    elif genre == "Stand-Up":
        colors.append("red")
    else:
        colors.append("gray")

# Inspect first 10 values of list
colors[:10]


fig = plt.figure(figsize=(12, 8))

plt.scatter(netflix_movies['release_year'], netflix_movies['duration'], c=colors)
plt.xlabel('Release year')
plt.ylabel("Duration (min)")
plt.title("Movie Duration by Year of Release")

answer = "no"