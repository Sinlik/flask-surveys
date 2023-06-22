from surveys import surveys, Question
responses = []

filename = "survey_responses.txt"
with open(filename, "w") as file:
    for response in responses:
        survey_name, question, answer = response
        file.write(f"Survey: {survey_name}\n")
        file.write(f"Question: {question}\n")
        file.write(f"Answer: {answer}\n\n")
print(f"Survey responses written to {filename}")