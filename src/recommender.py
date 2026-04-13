from typing import List, Dict, Tuple, Optional
from dataclasses import dataclass
import csv

@dataclass
class Song:
    """
    Represents a song and its attributes.
    Required by tests/test_recommender.py
    """
    id: int
    title: str
    artist: str
    genre: str
    mood: str
    energy: float
    tempo_bpm: float
    valence: float
    danceability: float
    acousticness: float

@dataclass
class UserProfile:
    """
    Represents a user's taste preferences.
    Required by tests/test_recommender.py
    """
    favorite_genre: str
    favorite_mood: str
    target_energy: float
    likes_acoustic: bool

class Recommender:
    """
    OOP implementation of the recommendation logic.
    Required by tests/test_recommender.py
    """
    def __init__(self, songs: List[Song]):
        self.songs = songs

    def recommend(self, user: UserProfile, k: int = 5) -> List[Song]:
        # TODO: Implement recommendation logic
        return self.songs[:k]

    def explain_recommendation(self, user: UserProfile, song: Song) -> str:
        # TODO: Implement explanation logic
        return "Explanation placeholder"

def load_songs(csv_path: str) -> List[Dict]:
    """
    Loads songs from a CSV file.
    Required by src/main.py
    """
    songs: List[Dict] = []
    numeric_fields = {
        "id": int,
        "energy": float,
        "tempo_bpm": float,
        "valence": float,
        "danceability": float,
        "acousticness": float,
    }

    with open(csv_path, newline="", encoding="utf-8") as csv_file:
        reader = csv.DictReader(csv_file)
        for row in reader:
            song = {}
            for key, value in row.items():
                if key in numeric_fields and value != "":
                    song[key] = numeric_fields[key](value)
                else:
                    song[key] = value
            songs.append(song)

    return songs

def score_song(user_prefs: Dict, song: Dict) -> Tuple[float, List[str]]:
    """
    Scores a single song against user preferences.
    Required by recommend_songs() and src/main.py
    """
    score = 0.0
    reasons: List[str] = []

    if user_prefs.get("genre") == song.get("genre"):
        score += 2.0
        reasons.append("Genre match (+2.0)")

    if user_prefs.get("mood") == song.get("mood"):
        score += 1.0
        reasons.append("Mood match (+1.0)")

    if "energy" in user_prefs and "energy" in song:
        energy_score = 1.0 - abs(user_prefs["energy"] - song["energy"])
        score += energy_score
        reasons.append(f"Energy similarity (+{energy_score:.2f})")

    if "tempo_bpm" in user_prefs and "tempo_bpm" in song:
        tempo_score = 1.0 - abs(user_prefs["tempo_bpm"] - song["tempo_bpm"]) / 180.0
        score += tempo_score
        reasons.append(f"Tempo similarity (+{tempo_score:.2f})")

    if "acousticness" in user_prefs and "acousticness" in song:
        acoustic_score = 1.0 - abs(user_prefs["acousticness"] - song["acousticness"])
        score += acoustic_score
        reasons.append(f"Acousticness similarity (+{acoustic_score:.2f})")

    return score, reasons

def recommend_songs(user_prefs: Dict, songs: List[Dict], k: int = 5) -> List[Tuple[Dict, float, str]]:
    """
    Functional implementation of the recommendation logic.
    Required by src/main.py
    """
    scored_songs: List[Tuple[Dict, float, List[str]]] = []

    for song in songs:
        score, reasons = score_song(user_prefs, song)
        scored_songs.append((song, score, reasons))

    scored_songs.sort(key=lambda item: item[1], reverse=True)

    return scored_songs[:k]
