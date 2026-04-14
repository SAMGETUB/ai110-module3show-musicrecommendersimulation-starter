"""
Command line runner for the Music Recommender Simulation.

This file helps you quickly run and test your recommender.

You will implement the functions in recommender.py:
- load_songs
- score_song
- recommend_songs
"""
from src.recommender import load_songs, recommend_songs
import csv


def main() -> None:
    songs = load_songs("data/songs.csv") 

    # Starter example profile
    pop_happy = {"genre": "pop", "mood": "happy", "energy": 0.8, "tempo_bpm": 120, "acousticness": 0.2}
    chill_lofi = {"genre": "lofi", "mood": "chill", "energy": 0.58, "tempo_bpm": 75, "acousticness": 0.80}
    intense_rock = {"genre": "rock", "mood": "intense", "energy": 0.91, "tempo_bpm": 152, "acousticness": 0.10}
    profile_a = {"genre": "ambient trance", "mood": "sad", "energy": 0.9, "tempo_bpm": 140, "acousticness": 0.1}
    profile_b = {"genre": "lounge jazz", "mood": "angry", "energy": 0.2, "tempo_bpm": 65, "acousticness": 0.85}

    # Change this to test different profiles
    user_prefs = intense_rock

    recommendations = recommend_songs(user_prefs, songs, k=5)

    for rank, rec in enumerate(recommendations, 1):
        song, score, explanation = rec
        print(f"{rank}. {song['title']} - Score: {score:.2f}")
        for reason in explanation:
         print(f"  - {reason}")
    print()

if __name__ == "__main__":
    main()
