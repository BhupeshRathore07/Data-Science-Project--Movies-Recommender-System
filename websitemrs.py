import pandas as pd
import streamlit as st
import pickle
import requests

st.set_page_config(layout="wide") # Website width = wide

#creating Poster Fetching Function
def fetch_poster(movie_id):
    response = requests.get("https://api.themoviedb.org/3/movie/{}?api_key=1208641ad3f3af4b74bec18fd5720146&language=en-US".format(movie_id))
    data = response.json()
    print(data)
    return "https://image.tmdb.org/t/p/w185/" + data["poster_path"]

# Creating recommendation function
def recommend(movie):
    movie_index = movies[movies['title'] == movie].index[0]
    distances = similarity[movie_index]
    movies_list = sorted(list(enumerate(distances)), reverse=True, key=lambda x: x[1])[1:6]
    recommendedMoviesPoster = []
    recommend_movies =[]
    for i in movies_list:
        movie_id = movies.iloc[i[0]].movie_id
        recommend_movies.append(movies.iloc[i[0]].title)

        #fetch poster from API
        recommendedMoviesPoster.append(fetch_poster(movie_id))

    return recommend_movies, recommendedMoviesPoster

#Accessing the Data
movies = pickle.load(open("movies_dict.pkl", "rb"))      #importing data in dictionary
movies = pd.DataFrame(movies)                            #creating data frame of dictionary
similarity = pickle.load(open("similarity.pkl", "rb"))

# Website title
st.title("Movie Recommender System")

#creating dropdown for movies selection
selected_movie_name= st.selectbox("Movies",movies['title'].values)

#creating recommend button
if st.button('Recommend'):
    name, poster = recommend(selected_movie_name)

    col1, col2, col3, col4, col5 = st.columns(5)

    with col1:
        st.text(name[0])
        st.image(poster[0])

    with col2:
        st.text(name[1])
        st.image(poster[1])

    with col3:
        st.text(name[2])
        st.image(poster[2])

    with col4:
        st.text(name[3])
        st.image(poster[3])

    with col5:
        st.text(name[4])
        st.image(poster[4])
