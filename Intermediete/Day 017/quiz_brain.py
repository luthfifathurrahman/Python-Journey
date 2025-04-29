class QuizBrain:
    def __init__(self, question_list):
        self.score = 0
        self.question_number = 0
        self.question_list = question_list

    def still_has_questions(self):
        return self.question_number < len(self.question_list)

    def next_question(self):
        q_text = self.question_list[self.question_number]
        self.question_number += 1
        user_answer = input(f"Q.{self.question_number}: {q_text.text} (True/False): ").lower()
        self.check_answer(user_answer, q_text.answer)

    def check_answer(self, user_answer, question_answer):
        if user_answer == question_answer.lower():
            self.score += 1
            print("Correct!")
        else:
            print("Wrong!")
        print(f"The correct answer: {question_answer}.")
        print(f"Your current score is: {self.score}/{self.question_number}")
        print("\n")