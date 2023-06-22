from flask import Flask, render_template, request
import sys
from surveys import surveys, Question
from flask_debugtoolbar import DebugToolbarExtension


app = Flask(__name__)
app.debug = True

app.config['SECRET_KEY'] = 'secret'
app.config['DEBUG_TB_ENABLED'] = True
app.config['DEBUG_TB_INTERCEPT_REDIRECTS'] = False

toolbar = DebugToolbarExtension(app)

@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        survey_key = request.form['survey']
        survey = surveys[survey_key]
        responses = []
        for question_index, question in enumerate(survey.questions, start=1):
            if question.allow_text:
                answer = request.form.get(f"{survey_key}_question_{question_index}")
                print(f"answer = {answer}")
            else:
                answer = request.form.get(f"{survey_key}_question_{question_index}_choice")
            responses.append((survey.title, question.question, answer))
            print(f"responses = {responses}")
        question.write_responses_to_file(responses, 'survey_responses.txt')
        return f"Survey {survey.title} responses saved succesfully!"
    else:
        return render_template('index.html', surveys=surveys)

if __name__ == '__main__':
    app.run()