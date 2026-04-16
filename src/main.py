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

    # Diverse user taste profiles for adversarial/edge-case testing
    user_prefs = [
        # 1. Impossible match: genre and mood not in dataset, extreme energy
        {
            "favorite_genre": "k-pop",
            "favorite_mood": "melancholy",
            "target_energy": 1.5,  # Out of normal range
            "likes_acoustic": True
        },
        # 2. Contradictory: likes acoustic but wants high energy and danceability
        {
            "favorite_genre": "jazz",
            "favorite_mood": "relaxed",
            "target_energy": 0.95,
            "target_danceability": 0.95,
            "target_acousticness": 0.95,
            "likes_acoustic": True
        },
        # 3. Diverse: prefers high valence, moderate tempo, and relaxed mood
        {
            "favorite_genre": "jazz",
            "favorite_mood": "relaxed",
            "target_valence": 0.7,
            "target_tempo": 90,
            "likes_acoustic": True
        }
    ]

    for i, profile in enumerate(user_prefs, 1):
        print(f"\n{'#' * 12} User Profile {i} {'#' * 12}")
        print("Profile:")
        for k, v in profile.items():
            print(f"  {k}: {v}")
        recommendations = recommend_songs(profile, songs, k=5)
        print("\nTop recommendations:\n")
        for idx, rec in enumerate(recommendations, 1):
            song, score, explanation = rec
            print("=" * 40)
            print(f"{idx}. Title      : {song['title']}")
            print(f"   Artist     : {song['artist']}")
            print(f"   Score      : {score:.2f}")
            print("   Reasons    :")
            for reason in explanation.split(';'):
                print(f"     - {reason.strip()}")
        print("=" * 40)


if __name__ == "__main__":
    main()
