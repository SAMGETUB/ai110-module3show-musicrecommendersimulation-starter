# 🎵 Music Recommender Simulation

## Project Summary

In this project you will build and explain a small music recommender system.

Your goal is to:

- Represent songs and a user "taste profile" as data
- Design a scoring rule that turns that data into recommendations
- Evaluate what your system gets right and wrong
- Reflect on how this mirrors real world AI recommenders

Replace this paragraph with your own summary of what your version does.

---

## How The System Works

Explain your design in plain language.
Real-world recommendation systems like Spotify use two main approaches. The first is collaborative filtering, which tracks your listening patterns and compares them to other users. If another user has the same listening habits as you and likes a song, the system recommends that song to you. The second is content-based filtering, which looks at the attributes of songs you listen to — like genre and artist and recommends other songs with similar attributes.

Our system uses content-based filtering. It scores each song based on how well it matches the user's preferences across five features: genre, mood, energy, tempo_bpm, and acousticness. The scoring recipe is: +2.0 points for a genre match, +1.0 point for a mood match, and an energy score calculated as 1 - abs(user_energy - song_energy) to reward songs closest to the user's target energy.

Algorithm Recipe
The system scores each song using the following rules:

Genre match: +2.0 points
Mood match: +1.0 point
Energy similarity: 1 - abs(user_energy - song_energy)
Tempo similarity: 1 - abs(user_tempo - song_tempo) / 180
Acousticness similarity: 1 - abs(user_acousticness - song_acousticness)

The maximum possible score is 6.0. Songs are ranked from highest to lowest score and the top 5 are returned.

Potential Bias
This system over-prioritizes genre and mood matching. A song that matches the user's genre gets +2.0 points regardless of how well its energy or tempo fits. This means a great song with the perfect energy and tempo but a different genre could rank lower than a mediocre genre match.


Some prompts to answer:

- What features does each `Song` use in your system
  - For example: genre, mood, energy, tempo
- What information does your `UserProfile` store
- How does your `Recommender` compute a score for each song
- How do you choose which songs to recommend

You can include a simple diagram or bullet list if helpful.

---

## Getting Started

### Setup

1. Create a virtual environment (optional but recommended):

   ```bash
   python -m venv .venv
   source .venv/bin/activate      # Mac or Linux
   .venv\Scripts\activate         # Windows

2. Install dependencies

```bash
pip install -r requirements.txt
```

3. Run the app:

```bash
python -m src.main
```

### Running Tests

Run the starter tests with:

```bash
pytest
```

You can add more tests in `tests/test_recommender.py`.

---

## Experiments You Tried

Pop Happy vs Chill Lofi:
The happy pop listener got upbeat, fast songs like Sunrise City and Gym Hero. The chill lofi listener got slow, calm songs like Midnight Coding and Library Rain. This makes sense because the two profiles are opposites in energy and tempo.
Intense Rock vs Profile A (ambient trance/sad):
The rock listener got Storm Runner at the top with a perfect score because every feature matched exactly. Profile A got similar high energy songs but no genre match, so the scores were much lower overall. The system could not find "ambient trance" in the catalog so it just recommended whatever had similar speed and energy.
Profile A vs Profile B:
Both adversarial profiles got zero genre and mood points because their genres don't exist in the catalog. Profile A got high energy songs, Profile B got slow calm songs  the only difference was their energy and tempo preferences since genre couldn't help.
---

## Limitations and Risks

Summarize some limitations of your recommender.

This recommender only works on a catalog of 18 songs, so results are very limited. It does not understand lyrics, artist style, or cultural context it only looks at numbers. It over-favors genre matching, which means users with niche or uncommon genres get poor recommendations. It also treats every user the same way, assuming one genre and one mood defines their entire taste.
---

## Reflection

Read and complete `model_card.md`:

[**Model Card**](model_card.md)

Write 1 to 2 paragraphs here about what you learned:

Building this recommender taught me that turning music taste into numbers is harder than it looks. The system works by comparing numbers if your energy target is 0.8 and a song has 0.82, it scores high. That simple math is the foundation of how real platforms like Spotify make suggestions, just at a much larger scale with millions of songs and users.

What surprised me most is how quickly bias shows up even in a simple system. Because genre is worth the most points, it controls almost every recommendation. If your favorite genre is not in the catalog, the system basically gives up on finding a real match. This made me realize that the decisions engineers make about weights and features are not just technical  they decide whose taste the system serves well and whose it ignores.
---

## 7. `model_card_template.md`

Combines reflection and model card framing from the Module 3 guidance. :contentReference[oaicite:2]{index=2}  

```markdown
# 🎧 Model Card - Music Recommender Simulation

## 1. Model Name

Give your recommender a name, for example:

> VibeFinder 1.0

---

## 2. Intended Use

- What is this system trying to do
- Who is it for

This recommender suggests songs from a small catalog based on a listener's favorite genre, mood, energy level, tempo, and how acoustic they like their music. It assumes the user has one clear taste profile. This is a classroom project — it is not meant for real users or production use.

---

## 3. How It Works (Short Explanation)

Describe your scoring logic in plain language.

The system looks at each song and gives it a score based on how well it matches what the user likes. Genre match gets the most points, mood match gets some points, and energy, tempo, and acousticness are scored by how close they are to what the user wants. Once every song has a score, the system sorts them and returns the top 5.
---

## 4. Data

Describe your dataset.

The catalog has 18 songs across genres like pop, lofi, rock, jazz, ambient, synthwave, indie pop, hip hop, folk, country, soul, and electronic. We started with 10 songs and added 8 more. Niche genres like ambient trance or lounge jazz are not represented.

---

## 5. Strengths

Where does your recommender work well

Works best for listeners with common genres like pop, lofi, or rock. Results feel accurate when preferences clearly match songs in the catalog. Every recommendation comes with a clear explanation of why it was chosen.

---

## 6. Limitations and Bias

Where does your recommender struggle
Our recommender has a clear weakness when it comes to genre. Because genre matching is worth the most points in our scoring system, songs that share the user's favorite genre will almost always appear at the top, even if other songs are a better fit in terms of energy or tempo. We discovered this during testing when we created user profiles with genres like "ambient trance" and "lounge jazz" that did not exist in our song catalog. Those users never received genre points at all, so the system had to rely only on speed and energy to make recommendations.

---

## 7. Evaluation

How did you check your system

We tested five different listener types to see how our recommender behaved. For someone who likes happy pop music, the results felt spot on upbeat pop songs came out on top every time. For a chill lofi listener, calm and slow songs dominated the list, which made sense. The intense rock listener got a perfect score for Storm Runner, which was surprising  it felt too perfect, like the system was cheating. When we tested two made-up listeners with unusual taste that didn't match any songs in our catalog, the recommender struggled and just guessed based on song speed and energy alone. We also did a quick experiment where we made energy matter more than genre  and suddenly pop songs started showing up in rock recommendations, which felt wrong. That told us genre is really important for keeping results on track.
---

## 8. Future Work

If you had more time, how would you improve this recommender

Add more songs and genres so niche listeners get better results
Add a diversity rule so the same artist does not appear too many times in the top 5
Let users set their own weights so they can decide what matters most to them
Add lyrics or artist style as a feature since two songs can have the same energy but feel completely different



---

## 9. Personal Reflection

Building this recommender showed me that even a simple system can feel surprisingly smart when the data lines up. What surprised me most was how much genre dominates the results. This changed how I think about apps like Spotify  behind all the magic, there are just numbers being compared and sorted. The tricky part is deciding which numbers matter most, and that decision always carries some bias.

