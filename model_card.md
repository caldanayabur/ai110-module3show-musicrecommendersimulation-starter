# 🎧 Model Card: Music Recommender Simulation

## 1. Model Name  

BeatBuddy

---

## 2. Intended Use  

This recommender is designed for classroom exploration and learning, not for real-world music streaming. It generates song recommendations from a small, fixed catalog based on a user's stated preferences for genre, mood, energy, and other features. The system assumes users know what they like and can specify their favorite genre, mood, and target values for features like tempo or valence. It is not intended for commercial use or for users with highly complex or evolving tastes.

---

## 3. How the Model Works  

The model looks at each song's features (like genre, mood, energy, tempo, valence, danceability, and acousticness) and compares them to what the user says they like. If a song matches the user's favorite genre or mood, it gets extra points. The model also checks if the song's numeric features (like tempo or valence) are close to the user's targets, and adds points if they are. For energy, it gives a higher score the closer the song's energy is to the user's target. After scoring all songs, it sorts them and recommends the top ones.

---

## 4. Data  

The dataset contains 20 songs, each with features like genre, mood, artist, energy, tempo, valence, danceability, and acousticness. Genres include pop, rock, jazz, lofi, synthwave, and more, with a variety of moods such as happy, intense, relaxed, and chill. No songs were added or removed from the starter set. Some genres and moods are underrepresented, and there are no songs with extremely high or low values for some features. The catalog is small, so it does not cover the full range of musical tastes or diversity found in real music libraries.

---

## 5. Strengths  

The system works well for users whose preferences match the genres and moods in the dataset. It gives clear, explainable recommendations, and the reasons for each pick are easy to understand. The model is good at finding songs that are close to the user's target energy, tempo, or valence. It is transparent, so users can see exactly why a song was recommended.

---

## 6. Limitations and Bias 

The model struggles with users whose preferences are outside the range of the dataset, such as those who want a genre or mood that isn't present, or an energy level higher than any song in the catalog. It can create "filter bubbles" by always recommending songs from the user's favorite genre or mood, ignoring other good matches. The system does not consider lyrics, artist popularity, or user listening history. One weakness found during experiments is that users with extreme or rare preferences (like very high energy) get only low-scoring, generic recommendations, making the system feel unresponsive for them. The model also does not promote diversity or surprise in its recommendations, so users may see the same types of songs repeatedly.

---


## 7. Evaluation

I tested the recommender using three different user profiles: one with impossible preferences (genre and mood not in the dataset, extreme energy), one with contradictory preferences (high acousticness, high energy, high danceability), and one with realistic but specific preferences (jazz, relaxed mood, high valence, moderate tempo, likes acoustic). For each profile, I checked if the top recommendations matched the user's stated preferences and if the explanations made sense. I also experimented with changing the genre weight, adding tempo and valence to the score, and disabling the mood check to see how the results changed. I was surprised that users with extreme or rare preferences always got low scores and generic recommendations, while users with more typical preferences got clear, relevant results. The experiments helped reveal where the model is strong and where it fails to adapt to unusual user needs.

---

## 8. Future Work  


If I extended this project, I would swap out all the songs in the dataset for tracks from my own music library. This would let me test the recommender with my real preferences and see if it can actually give good suggestions. I would also look for ways to add more features, handle more complex or specific user tastes, and improve the diversity of recommendations so users don’t always get the same types of songs.

---

## 9. Personal Reflection  


Building this recommender showed me how complex real music apps like Spotify must be, since they serve millions of users and use far more features than my simple system. I learned it’s hard to recommend music to people with very specific tastes. For example, users with extreme preferences only got low-scoring, generic results, which made the system feel unhelpful for them. I also realized how much human judgment still matters, because the model can only use the features it has and might miss what really makes a song enjoyable for someone. I was surprised that even a simple scoring system could still feel somewhat personalized. I also found it important to double-check the changes suggested by AI tools, to make sure the code still made sense.
