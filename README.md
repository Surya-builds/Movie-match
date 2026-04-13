MovieMatch – Movie Recommendation System

MovieMatch is a content-based movie recommendation web app built using the TMDB 5000 Movies Dataset and deployed with Streamlit Cloud.

The app suggests movies similar to the one selected by the user and fetches live movie posters using the TMDB API.

⸻

🚀 Features
	•	🎥 Recommend 6 similar movies instantly
	•	🖼️ Live movie poster fetching using TMDB API
	•	✨ Clean and modern Streamlit UI
	•	📱 Responsive 3 × 2 movie card layout
	•	⚡ Fast loading with compressed similarity matrix
	•	☁️ Fully deployed on Streamlit Cloud

⸻

🛠️ Tech Stack
	•	Python
	•	Pandas
	•	NumPy
	•	Scikit-learn
	•	Streamlit
	•	Requests
	•	TMDB API

⸻

📂 Dataset

Dataset used: TMDB 5000 Movies Dataset

Files used:
	•	tmdb_5000_movies.csv
	•	tmdb_5000_credits.csv

⸻

🧠 Model Used

This project uses a content-based filtering recommendation system.

Movies are recommended based on:
	•	genres
	•	keywords
	•	cast
	•	crew
	•	overview

A cosine similarity matrix is used to find the closest matching movies.

⸻

⚙️ Optimizations Done

I downloaded an existing repository and significantly improved it by:
	•	fixing file path and deployment errors
	•	replacing deprecated Streamlit functions
	•	compressing the large similarity matrix from 176 MB to 26 MB
	•	improving UI and layout
	•	fixing GitHub large file issues
	•	successfully deploying the app
