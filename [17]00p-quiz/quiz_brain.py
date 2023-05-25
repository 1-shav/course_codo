class QuizBrain:

    def __init__(self, list):
        self.question_num = 0
        self.question_list = list
        self.score = 0

    def still_has_questions(self):
        return self.question_num < len(self.question_list)

    def next_question(self):
        current_question = self.question_list[self.question_num]
        self.question_num += 1
        user_ans = input(f"Q.{self.question_num}: {current_question.text} (True/False)?: ")
        self.check_answer(user_ans, current_question.answer)

    def check_answer(self, user_ans, correct_ans):
        if user_ans.lower() == correct_ans.lower():
            print("You got it right!")
            self.score += 1
        else:
            print("That's wrong")
        print(f"The correct answer was: {correct_ans}")
        print(f"Your current score is: {self.score}/{self.question_num}")
        print("\n")