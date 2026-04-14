# 🎧 Model Card: Music Recommender Simulation

## 1. Model Name  

Give your model a short, descriptive name.  
VibeMatch 1.0
---

## 2. Intended Use  

Describe what your recommender is designed to do and who it is for. 

This recommender suggests songs from a small catalog based on a listener's favorite genre, mood, energy level, tempo, and how acoustic they like their music. It assumes the user has one clear taste profile. This is a classroom project — it is not meant for real users or production use.

---

## 3. How the Model Works  

The system looks at each song in the catalog and gives it a score based on how well it matches what the user likes. If the song's genre matches the user's favorite, it gets the most points. If the mood matches, it gets more points. For energy, tempo, and acousticness, the system measures how close the song is to what the user wants — the closer, the more points. Once every song has a score, the system sorts them and returns the top 5.
---

## 4. Data  

Describe the dataset the model uses.  

The catalog has 18 songs across genres like pop, lofi, rock, jazz, ambient, synthwave, indie pop, hip hop, folk, country, soul and electronic. We started with 10 songs and added 8 more to improve variety. The dataset is small and mostly reflects mainstream Western music taste. Niche genres like ambient trance or lounge jazz are not represented.

---

## 5. Strengths  

Where does your system seem to work well  

The system works best for listeners with common genres like pop, lofi, or rock since those are well represented in the catalog. When the user's preferences clearly match songs in the dataset, the results feel intuitive and accurate. The scoring is also transparent — every recommendation comes with a clear explanation of why it was chosen.

---

## 6. Limitations and Bias 

Where the system struggles or behaves unfairly. 

Our recommender has a clear weakness when it comes to genre. Because genre matching is worth the most points in our scoring system, songs that share the user's favorite genre will almost always appear at the top, even if other songs are a better fit in terms of energy or tempo. We discovered this during testing when we created user profiles with genres like "ambient trance" and "lounge jazz" that did not exist in our song catalog. Those users never received genre points at all, so the system had to rely only on speed and energy to make recommendations

---

## 7. Evaluation  

How you checked whether the recommender behaved as expected. 

We tested five different listener types to see how our recommender behaved. For someone who likes happy pop music, the results felt spot on  upbeat pop songs came out on top every time. For a chill lofi listener, calm and slow songs dominated the list, which made sense. The intense rock listener got a perfect score for Storm Runner, which was surprising it felt too perfect, like the system was cheating. When we tested two made-up listeners with unusual taste that didn't match any songs in our catalog, the recommender struggled and just guessed based on song speed and energy alone. We also did a quick experiment where we made energy matter more than genre  and suddenly pop songs started showing up in rock recommendations, which felt wrong. That told us genre is really important for keeping results on track.

---

## 8. Future Work  

Ideas for how you would improve the model next.  

Add more songs and genres so niche listeners get better results
Add a diversity rule so the same artist does not appear too many times in the top 5
Let users set their own weights so they can decide what matters most to them
Add lyrics or artist style as a feature since two songs can have the same energy but feel completely different

---

## 9. Personal Reflection  

A few sentences about your experience.  

Prompts:  

Building this recommender showed me that even a simple system can feel surprisingly smart when the data lines up. What surprised me most was how much genre dominates the results one feature can control everything if its weight is too high. This changed how I think about apps like Spotify. Behind all the magic, there are just numbers being compared and sorted. The tricky part is deciding which numbers matter most, and that decision always carries some bias.