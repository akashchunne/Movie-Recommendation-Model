import streamlit as st
import pandas as pd
import pickle

def recommend(movie):
    movie_index = movies[movies['title']==movie].index[0]
    distance = similarity[movie_index]
    movie_list = sorted(list(enumerate(distance)),reverse=True,key=lambda x:x[1])[1:6]
    recommended_movies = []
    for i in movie_list:
        recommended_movies.append(movies.iloc[i[0]].title)
    return recommended_movies


movie_dict = pickle.load(open('movie_dict.pkl', 'rb'))
movies = pd.DataFrame(movie_dict)
similarity = pickle.load(open('similarity.pkl', 'rb'))
st.title("Movie Recommendation System")

Selected_movie_name = st.selectbox("Enter the name of Movie",movies['title'].values)

if st.button("Recommend"):
    recommendations = recommend(Selected_movie_name)
    for i in recommendations:
        st.write(i)
