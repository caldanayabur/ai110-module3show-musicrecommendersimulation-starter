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

The `Recommender` system should store a list of songs, then use a Gaussian scoring function to compute one score per feature, then weighted average those scores to get a final score for each song. Each feature should have weight, for example, genre should have more weight than mood because genre is more specific to an user's taste.

Each `Song` should use the features energy, tempo_bpm, valence, danceability, acousticness, genre, and mood.

`UserProfile` should store the user's favorite genre, favorite mood, target energy, and if they like acoustic music.

The songs with the highest scores are recommended to the user. I want for the user to be able to specify how many songs they want to be recommended.
---

**What features does each Song use?**
- genre, mood, artist, energy, tempo_bpm, valence, danceability, acousticness

**What information does your UserProfile store?**
- favorite genre, favorite mood, favorite artist (optional), target energy, target tempo, target valence, target danceability, target acousticness, number of recommendations wanted

**How does your Recommender compute a score for each song?**
- For each song, add points for matching genre (+2), mood (+1), artist (+1), and for being close to the user's targets for energy, tempo, valence, danceability, and acousticness (+1 each if within a threshold). Add a similarity score for energy (1 - absolute difference).

**How do you choose which songs to recommend?**
- After scoring all songs, sort them by score and recommend the top K songs as requested by the user.

---

**Data Flow Diagram (Mermaid.js):**

```mermaid
flowchart TD
  A[User Preferences (Genre, Mood, Energy, etc.)] --> B[Load Songs from CSV]
  B --> C{For each Song}
  C --> D[Compute Score:\n  +2 Genre match\n  +1 Mood match\n  +1 Artist match\n  +1 Tempo close\n  +1 Danceability close\n  +1 Acousticness close\n  +1 Valence close\n  +Similarity for Energy]
  D --> E[Store Song & Score]
  E --> F{All Songs Scored?}
  F -- No --> C
  F -- Yes --> G[Sort Songs by Score]
  G --> H[Select Top K Songs]
  H --> I[Output: Recommendations]
```

---

**Potential Bias Note:**  
This system might over-prioritize genre, so it could ignore great songs that match the user's mood or other preferences but are in a different genre. It may also favor songs with features close to the user's targets, even if those features are less important to the user.

---

Recommendations output:
![alt text](Output.png)



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

Use this section to document the experiments you ran. For example:

- What happened when you changed the weight on genre from 2.0 to 0.5
- What happened when you added tempo or valence to the score
- How did your system behave for different types of users

---

## Limitations and Risks

Summarize some limitations of your recommender.

Examples:

- It only works on a tiny catalog
- It does not understand lyrics or language
- It might over favor one genre or mood

You will go deeper on this in your model card.

---

## Reflection

Read and complete `model_card.md`:

[**Model Card**](model_card.md)

Write 1 to 2 paragraphs here about what you learned:

- about how recommenders turn data into predictions
- about where bias or unfairness could show up in systems like this


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

Example:

> This model suggests 3 to 5 songs from a small catalog based on a user's preferred genre, mood, and energy level. It is for classroom exploration only, not for real users.

---

## 3. How It Works (Short Explanation)

Describe your scoring logic in plain language.

- What features of each song does it consider
- What information about the user does it use
- How does it turn those into a number

Try to avoid code in this section, treat it like an explanation to a non programmer.

---

## 4. Data

Describe your dataset.

- How many songs are in `data/songs.csv`
- Did you add or remove any songs
- What kinds of genres or moods are represented
- Whose taste does this data mostly reflect

---

## 5. Strengths

Where does your recommender work well

You can think about:
- Situations where the top results "felt right"
- Particular user profiles it served well
- Simplicity or transparency benefits

---

## 6. Limitations and Bias

Where does your recommender struggle

Some prompts:
- Does it ignore some genres or moods
- Does it treat all users as if they have the same taste shape
- Is it biased toward high energy or one genre by default
- How could this be unfair if used in a real product

---

## 7. Evaluation

How did you check your system

Examples:
- You tried multiple user profiles and wrote down whether the results matched your expectations
- You compared your simulation to what a real app like Spotify or YouTube tends to recommend
- You wrote tests for your scoring logic

You do not need a numeric metric, but if you used one, explain what it measures.

---

## 8. Future Work

If you had more time, how would you improve this recommender

Examples:

- Add support for multiple users and "group vibe" recommendations
- Balance diversity of songs instead of always picking the closest match
- Use more features, like tempo ranges or lyric themes

---

## 9. Personal Reflection

A few sentences about what you learned:

- What surprised you about how your system behaved
- How did building this change how you think about real music recommenders
- Where do you think human judgment still matters, even if the model seems "smart"

