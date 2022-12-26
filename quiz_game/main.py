
from question_model import Question
import data
import quiz_brain

question_bank = []
q_data = data.question_data

for number in range(0,len(q_data)-1):
    question_text = q_data[number]["text"]
    question_answer = q_data[number]["answer"]
    new_question = Question(text=question_text,answer=question_answer)
    question_bank.append(new_question)


quiz = quiz_brain.Quiz(question_bank)
while quiz.still_has_question():
    quiz.question_next()



