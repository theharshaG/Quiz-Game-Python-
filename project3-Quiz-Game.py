import random

questions = [
    {"q": "Capital of India?", "a": "delhi"},
    {"q": "2 + 2=?", "a": "4"},
    {"q": "Python is language?[yes/no]", "a": "yes"},
    {"q": "what is OOP ?","a":"object oriented program"}
]
score=0
total_questions = len(questions)
random.shuffle(questions)

for i,items in enumerate(questions,start=1):
    print(i,",",items["q"])
    
    ans=input("your answer:").strip().lower()
    
    if ans==items["a"]:
        print("correct..")
        score += 1 
    else:
        print(f"Wrong! The correct answer is: {items['a']}")


print(f"You got {score} out of {total_questions}")
