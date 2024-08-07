#Code with poster But max tile limit is exceeding
import streamlit as st 
import pickle
import pandas as pd
import requests

def fetch_poster(movie_id):
    url = f"https://api.themoviedb.org/3/movie/{movie_id}?api_key=bbb029ce7315583b5d3fc11aa8a5f7e7&language=en-US"
    data = requests.get(url).json()
    poster_path = data['poster_path']
    full_path = "https://image.tmdb.org/t/p/w500/" + poster_path
    return full_path

def fetch_description(movie_id):
    url = f"https://api.themoviedb.org/3/movie/{movie_id}?api_key=bbb029ce7315583b5d3fc11aa8a5f7e7&language=en-US"
    data = requests.get(url).json()
    description = data['overview']
    return description

def recommend(movie):
    movie_index = movies[movies['title'] == movie].index[0]
    distances = similarity[movie_index]
    movies_list = sorted(list(enumerate(distances)), reverse=True, key=lambda x: x[1])[1:6]
    recommended_movies = []
    recommended_movie_posters = []
    recommended_movie_descriptions = []
    for i in movies_list:
        movie_id = movies.iloc[i[0]].movie_id
        recommended_movies.append(movies.iloc[i[0]].title)
        recommended_movie_posters.append(fetch_poster(movie_id))
        recommended_movie_descriptions.append(fetch_description(movie_id))
    return recommended_movies, recommended_movie_posters, recommended_movie_descriptions

movie_dict = pickle.load(open('movies.pkl', 'rb'))
movies = pd.DataFrame(movie_dict)
similarity = pickle.load(open('similarity_1.pkl', 'rb'))

st.title('Movie Recommendation System')

selected_movie_name = st.selectbox('Select a movie', movies['title'].values)

if st.button('Show recommendation'):
    recommendations, posters, descriptions = recommend(selected_movie_name)
    for i in range(len(recommendations)):
        st.write(f"**{recommendations[i]}**")
        st.image(posters[i])
        st.write(descriptions[i])
