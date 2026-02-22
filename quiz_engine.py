import random

class QuizEngine:
    def __init__(self):
        self.questions = {}
        self.used_questions = set()

    def generate_question(self, difficulty):
        if difficulty < 1 or difficulty > 100:
            raise ValueError("Difficulty must be between 1 and 100.")
        if difficulty in self.used_questions:
            raise Exception("No more questions available for this difficulty level.")

        # Simulate question creation based on difficulty
        question_text = f"What is the capital of country with difficulty level {difficulty}?"
        correct_answer = "Example Answer"
        options = self.generate_options(correct_answer)

        self.questions[difficulty] = {
            'question': question_text,
            'options': options,
            'correct_answer': correct_answer
        }
        self.used_questions.add(difficulty)

        return self.questions[difficulty]

    def generate_options(self, correct_answer):
        # Simulate generation of three wrong answers
        wrong_answers = set()
        while len(wrong_answers) < 3:
            wrong_answer = f"Wrong Answer {random.randint(1, 100)}"
            wrong_answers.add(wrong_answer)
        options = list(wrong_answers) + [correct_answer]
        random.shuffle(options)
        return options

# Example usage
quiz = QuizEngine()
try:
    question = quiz.generate_question(5)  # Example for difficulty level 5
    print(question)
except Exception as e:
    print(e)