class Question:
    """Question on a questionnaire."""

    def __init__(self, question, choices=None, allow_text=False):
        """Create question (assume Yes/No for choices."""

        if not choices:
            choices = ["Yes", "No"]

        self.question = question
        self.choices = choices
        self.allow_text = allow_text

    
    def write_responses_to_file(self, responses, filename):
        with open(filename, 'w') as file:
            for response in responses:
                survey_name, question, answer = response
                file.write(f"Survey: {survey_name}\n")
                file.write(f"Question: {question}\n")
                file.write(f"Answer: {answer}\n\n")

    def get_answer(self):
        if self.allow_text:
            answer = input(f"{self.question} ({'/'.join(self.choices)}): ")
            return answer, f"Answer: {answer}"
        else:
            while True:
                answer = input(f"{self.question} ({'/'.join(self.choices)}): ")
                if answer in self.choices:
                    return answer
                else:
                    print("Incorrect Answer, try again.")


class Survey:
    """Questionnaire."""

    def __init__(self, title, instructions, questions):
        """Create questionnaire."""

        self.title = title
        self.instructions = instructions
        self.questions = questions

    def conduct_survey(self):
        print(self.title)
        print(self.instructions)
        responses = []
        for question in self.questions:
            answer = question.get_answer()
            responses.append((self.title, question.question, answer))
        print("Done Survey!")
        return responses
    
satisfaction_survey = Survey(
    "Customer Satisfaction Survey",
    "Please fill out a survey about your experience with us.",
    [
        Question("Have you shopped here before?"),
        Question("Did someone else shop with you today?"),
        Question("On average, how much do you spend a month on frisbees?",
                 ["Less than $10,000", "$10,000 or more"]),
        Question("Are you likely to shop here again?"),
    ])

personality_quiz = Survey(
    "Rithm Personality Test",
    "Learn more about yourself with our personality quiz!",
    [
        Question("Do you ever dream about code?"),
        Question("Do you ever have nightmares about code?"),
        Question("Do you prefer porcupines or hedgehogs?",
                 ["Porcupines", "Hedgehogs"]),
        Question("Which is the worst function name, and why?",
                 ["do_stuff()", "run_me()", "wtf()"],
                 allow_text=True),
    ]
)

books_survey = Survey(
    "Books Survey",
    "Fill out the following",
    [
        Question("Do you like Dairy of a Wimpy Kid?"),
        Question("What is your favoruite book?", 
                 allow_text=True),
        Question("Are you interverted or exterverted?", 
                 ["Intervert", "Extervert"]),
        Question("Do you write your own books?"),
        Question("How well do you know books?", ["Very well", "So-so", "I'm a writer and author and storyteller!", "I hate books", "Don't say that word again!"]),
        Question("Test")
    ]
)

about_qa = Survey(
    "About You",
    "Fill out the questions so we can learn more about you",
    [
        Question("How old are you?", allow_text=True),
        Question("What is your level of programming?", ["Begginer", "Intermedient", "Advanced"]),
        Question("What is your first name?", allow_text=True),
        Question("What is your last name?", allow_text=True),
        Question("Why do you want to learn about programming?", allow_text=True)
    ]
)

surveys = {
    "satisfaction": satisfaction_survey,
    "personality": personality_quiz,
    "books": books_survey,
    "about": about_qa
}