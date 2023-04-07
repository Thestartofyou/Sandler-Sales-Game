import random

class SandlerSellingGame:
    def __init__(self):
        self.questions = {
            "What are your current challenges?": "Uncover Pain Points",
            "How are you currently addressing those challenges?": "Qualify the Prospect",
            "What happens if you don't solve these challenges?": "Uncover Pain Points",
            "What are your objectives?": "Qualify the Prospect",
            "Can you tell me more about your decision-making process?": "Qualify the Prospect",
            "What would success look like for you?": "Uncover Pain Points"
        }

    def run(self):
        print("Welcome to the Sandler Selling Game!")
        print("The objective of the game is to match the correct Sandler Rule to each question.")
        print("Let's get started!")
        print("")

        questions = list(self.questions.keys())
        random.shuffle(questions)

        score = 0

        for question in questions:
            print("Question: ", question)
            answer = input("Enter the Sandler Rule that best applies to this question: ")

            if answer == self.questions[question]:
                print("Correct!")
                score += 1
            else:
                print("Incorrect. The correct answer is: ", self.questions[question])
            print("")

        print("Game over!")
        print("Your score is: ", score)

if __name__ == "__main__":
    game = SandlerSellingGame()
    game.run()
