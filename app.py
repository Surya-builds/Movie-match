import pickle
import numpy as np
import streamlit as st
import requests
# Page config
st.set_page_config(
    page_title="MovieMatch",
    page_icon="🎬",
    layout="centered"
)

# Custom CSS
st.markdown("""
<style>
.block-container {
    max-width: 1000px;
    padding-top: 2rem;
    margin: auto;
}

.stButton button {
    background: linear-gradient(90deg, #ff4b2b, #ff416c);
    color: white;
    border-radius: 12px;
    height: 50px;
    font-size: 18px;
    font-weight: 600;
    border: none;
    width: 100%;
}

h1 {
    text-align: center;
    color: #ff416c;
    font-size: 42px;
}

img {
    border-radius: 18px;
    transition: transform 0.25s ease, box-shadow 0.25s ease;
}

img:hover {
    transform: scale(1.03);
}
</style>
""", unsafe_allow_html=True)


# Fetch movie poster
def fetch_poster(movie_id):
    url = f"https://api.themoviedb.org/3/movie/{movie_id}?api_key=8265bd1679663a7ea12ac168da84d2e8&language=en-US"
    data = requests.get(url).json()

    poster_path = data.get("poster_path")
    if poster_path:
        return "https://image.tmdb.org/t/p/w500/" + poster_path
    return None


# Recommend movies
def recommend(movie):
    index = movies[movies["title"] == movie].index[0]

    distances = sorted(
        list(enumerate(similarity[index])),
        reverse=True,
        key=lambda x: x[1]
    )

    recommended_movie_names = []
    recommended_movie_posters = []

    # 6 movies
    for i in distances[1:7]:
        movie_id = movies.iloc[i[0]].movie_id
        recommended_movie_names.append(movies.iloc[i[0]].title)
        recommended_movie_posters.append(fetch_poster(movie_id))

    return recommended_movie_names, recommended_movie_posters


# Load files
movies = pickle.load(open("movie_list.pkl", "rb"))
similarity = np.load("similarity.npz")["similarity"]

movie_list = movies["title"].values

# Header
st.markdown("<h1>🎬 MovieMatch</h1>", unsafe_allow_html=True)
st.markdown(
    "<p style='text-align:center;color:gray;'>Find movies similar to your favorites instantly</p>",
    unsafe_allow_html=True
)

# Movie selector
selected_movie = st.selectbox(
    "Choose a movie",
    movie_list
)

# Show recommendations
if st.button("✨ Show Recommendations"):
    with st.spinner("🎬 Fetching your movie recommendations..."):
        names, posters = recommend(selected_movie)

    # First row
    row1 = st.columns(3)
    for i in range(3):
        with row1[i]:
            st.image(posters[i], use_container_width=True)
            st.markdown(f"### 🎥 {names[i]}")

    st.markdown("<br>", unsafe_allow_html=True)

    # Second row
    row2 = st.columns(3)
    for i in range(3, 6):
        with row2[i - 3]:
            st.image(posters[i], use_container_width=True)
            st.markdown(f"### 🎥 {names[i]}")