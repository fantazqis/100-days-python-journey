class QuizBrain:
    def __init__(self, q_list):
        self.question_number = 0
        self.question_list = q_list
        self.score = 0

    def next_question(self):
        current_question = self.question_list[self.question_number]
        print(f"hehehe: {current_question}")
        self.question_number += 1
        user_input = input(f"Question {self.question_number}: {current_question.question_text} (True/False): ")
        self.check_answer(user_input, current_question.answers)
        print(f"your current score is {self.score}/{self.question_number}")

    def still_has_questions(self):
        return self.question_number < len(self.question_list)

    def check_answer(self, user_input, correct_answer):
        if user_input.lower() == correct_answer.lower():
            print(f"Correct!")
            self.score += 1

        elif user_input.lower() != correct_answer.lower():
            print(f"Wrong!")

        print("the correct answer was: ", correct_answer)