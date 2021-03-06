#author: Fatemeh
import pandas as pd

!ls "C:\kiaie\Data Science and ML\Edx-python for DS\\movielens"

#see the word count line.. number of movies.. UNIX commands with !
!cat ./movielens/movies.csv | wc -l

movies = pd.read_csv('./movielens/movies.csv', sep=',')
print(type(movies))
movies.head(15)


# Timestamps represent seconds since midnight Coordinated Universal Time (UTC) of January 1, 1970
#files are: tags, ratings, 
#.head func by default shows first "5" rows
tags = pd.read_csv('./movielens/tags.csv', sep=',')
tags.head()

ratings = pd.read_csv('./movielens/ratings.csv', sep=',', parse_dates=['timestamp'])
ratings.head()

#showing the shapes of movie matrics
movies.shape
