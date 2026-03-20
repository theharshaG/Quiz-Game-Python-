# Quiz-Game-Python

# Quiz Game (Python)

##  Project Overview

This project is a simple **Quiz Game** built using Python.
The program asks multiple questions, checks user answers, and calculates the final score.

Questions are shuffled randomly each time, making the quiz dynamic and interesting.

##  Features

* Multiple quiz questions
* Random question order
* Score calculation
* Instant feedback (correct / wrong)
* Case-insensitive answer checking

##  Technologies Used

* Python
* `random` module

## How the Program Works

### 1️ Questions Storage
Questions are stored as a list of dictionaries:

```python id="7z6kdp"
{"q": "Capital of India?", "a": "delhi"}
```

### 2️ Randomization

Questions are shuffled using:

```python id="3f4d4r"
random.shuffle(questions)
```

So each time the quiz order changes.

### 3️ Answer Checking

* User input is converted to lowercase
* Compared with correct answer

```python id="c2ny1u"
ans = input().strip().lower()
```

### 4️ Score Calculation

* Each correct answer increases score
* Final score is displayed at the end

Example:

```id="sh3cce"
You got 3 out of 4
```

##  How to Run

1. Install Python
2. Save file as `quiz.py`
3. Run the program:

```bash id="k64qj7"
python quiz.py
```

## Concepts Used

* Lists and Dictionaries
* Loops (`for`)
* Conditional statements
* String handling
* Randomization
* 
##  Learning Outcomes

After completing this project, you will learn:
* How to build interactive programs
* How to use lists of dictionaries
* How to randomize data
* How to validate user input
* How quiz systems work

##  Possible Improvements

* Add more questions
* Add timer for each question
* Store score in a file
* Add difficulty levels
* Create GUI version using Tkinter
* Add leaderboard system

##  Author

Harsha G
Learning **Python | Embedded Systems | IoT**
