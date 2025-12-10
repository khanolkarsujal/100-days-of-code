from  data import question_data
from question_model import Question
from quiz_brain import QuizBrain



question_bank = []

for q in question_data:
    new_text = q["text"]
    new_answer = q["answer"]
    new_q = Question(new_text,new_answer)
    question_bank.append(new_q)
    

quiz = QuizBrain(question_bank)

while quiz.still_has_question():
    quiz.next_question()
    

print("You have complete the quiz")
print(f"Your final score was {quiz.score}/{quiz.question_number}")