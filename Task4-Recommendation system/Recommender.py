import numpy as np
import pandas as pd
import difflib
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity

MOVIE_Dataset = pd.read_csv('D:\X internship\TASK NO 3\movies.csv')

# selecting the relevant features for recommendation
selected_features = ['genres','keywords','tagline','cast','director']

for feature in selected_features:
  MOVIE_Dataset[feature] = MOVIE_Dataset[feature].fillna('')

# combining 5 selected features
common_features = MOVIE_Dataset['genres']+' '+MOVIE_Dataset['keywords']+' '+MOVIE_Dataset['tagline']+' '+MOVIE_Dataset['cast']+' '+MOVIE_Dataset['director']

# converting the text data to feature vectors
vectorizer = TfidfVectorizer()
Vectors = vectorizer.fit_transform(common_features)

# getting the similarity scores using cosine similarity
similarity = cosine_similarity(Vectors)

def recommend(movie_name):
    # finding the close match
    LIST_Titles = MOVIE_Dataset['title'].tolist()
    finding_close_match = difflib.get_close_matches(movie_name, LIST_Titles)
    close_match = finding_close_match[0]
    index_movie_list = MOVIE_Dataset[MOVIE_Dataset.title == close_match]['index'].values[0]
    similarity_score = list(enumerate(similarity[index_movie_list]))
    sorted_similar_movies = sorted(similarity_score, key=lambda x: x[1], reverse=True)
    return [MOVIE_Dataset[MOVIE_Dataset.index == i[0]]['title'].values[0] for i in sorted_similar_movies[:30]]
