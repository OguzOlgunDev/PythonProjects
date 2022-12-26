class Quiz:
    def __init__(self, q_list):
        self.question_number = 0
        self.question_score = 0
        self.question_list = q_list


    def question_next(self):
        current_question = self.question_list[self.question_number]
        self.question_number += 1
        answer = input(f"Q {self.question_number}:{current_question.text}  (True/False)")
        self.score(answer,current_question.answer)

    def score(self,answer,correct_answer):
        if answer.lower() == correct_answer.lower():
            self.question_score +=1
        print(f"{self.question_score} / {self.question_number}")

    def still_has_question(self):
        return self.question_number < len(self.question_list)
