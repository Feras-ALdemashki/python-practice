from questions import trivia_questions
import random 
print("you will get 7 questions to answer Good luck!")

def trivia_game(question_set):
    questions = question_set[:]      
    random.shuffle(questions)

    score = 0
    q_tracker = 0

    for q in questions:
        if q_tracker >= 7:
            break

        print(q["question"])
        print(q["choices"])

        u_choice = input("please select your answer: ")
        q_tracker += 1

        if u_choice == q["answer"]:
            score += 1
            print(f"right answer your score is {score}")
        else:
            print(f"wrong answer your score is {score}")
    print(f'final score is {score}')



trivia_game(trivia_questions)