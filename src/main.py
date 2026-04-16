"""
Command line runner for the Music Recommender Simulation.

This file helps you quickly run and test your recommender.

You will implement the functions in recommender.py:
- load_songs
- score_song
- recommend_songs
"""

from recommender import load_songs, recommend_songs


def main() -> None:
    songs = load_songs("data/songs.csv") 


    # User taste profile for recommendations
    user_prefs = {
        "favorite_genre": "rock",
        "favorite_mood": "intense",
        "target_energy": 0.9,
        "likes_acoustic": False
    }

    recommendations = recommend_songs(user_prefs, songs, k=5)

    print("\nTop recommendations:\n")
    for idx, rec in enumerate(recommendations, 1):
        song, score, explanation = rec
        print("=" * 40)
        print(f"{idx}. Title      : {song['title']}")
        print(f"   Artist     : {song['artist']}")
        print(f"   Score      : {score:.2f}")
        print("   Reasons    :")
        # Split explanation into bullet points if multiple reasons
        for reason in explanation.split(';'):
            print(f"     - {reason.strip()}")
    print("=" * 40)


if __name__ == "__main__":
    main()
