import streamlit as st
import pickle
import pandas as pd
# import requests

# def fetch_poster(movie_id):
#     url = "https://api.themoviedb.org/3/movie/{}?api_key=bbb029ce7315583b5d3fc11aa8a5f7e7&language=en-US".format(movie_id)
#     data = requests.get(url)
#     data = data.json()
#     poster_path = data['poster_path']
#     full_path = "https://image.tmdb.org/t/p/w500/" + poster_path
#     return full_path

def recommend(movie):
    movie_index = movies[movies['title'] == movie].index[0]
    distances = similarity[movie_index]
    movies_list = sorted(list(enumerate(distances)), reverse=True, key=lambda x: x[1])[1:6]
    recommended_movies = []
    # recommended_movie_posters = []
    for i in movies_list:
        # fetch the movie poster
        # movie_id = movies.iloc[i[0]].movie_id
        # recommended_movie_posters.append(fetch_poster(movie_id))
        recommended_movies.append(movies.iloc[i[0]].title)

    return recommended_movies

# Load the movie data and similarity matrix
movie_dict = pickle.load(open('movies.pkl', 'rb'))
movies = pd.DataFrame(movie_dict)  # Corrected this line
similarity = pickle.load(open('similarity_1.pkl', 'rb'))

# Title and description
st.title('Movie Recommendation System')
st.markdown("### Select a movie to get recommendations")

# Select movie
selected_movie_name = st.selectbox('Select a movie', movies['title'].values)

# Create columns for buttons
col1, col2 = st.columns(2)

# Show recommendations
with col1:
    show_recommend_button = st.button('Show recommendation')

with col2:
    reset_button = st.button('Reset')

if show_recommend_button:
    recommendations = recommend(selected_movie_name)
    st.markdown(f"### Movies recommended for **{selected_movie_name}**:")
    for i, movie in enumerate(recommendations, start=1):
        st.markdown(f"{i}. **{movie}**")

if reset_button:
    st.rerun()
