#author: Fatemeh
import pandas as pd

!ls "C:\kiaie\Data Science and ML\Edx-python for DS\\movielens"

#see the word count line.. number of movies.. UNIX commands with !
!cat ./movielens/movies.csv | wc -l

movies = pd.read_csv('./movielens/movies.csv', sep=',')
print(type(movies))
movies.head(15)


