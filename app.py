#from flask import Flask, render_template
#
#
#app = Flask(__name__)
#
#@app.route('/')
#def index():
#    return render_template('index.html')
#
#
#if __name__ == "__main__":
#
#    app.run(debug=True)


from flask import Flask, render_template, request

app = Flask(__name__)

# Define a list of quiz questions and answers
questions = [
    {
        "question": "What is AWS S3?",
        "choices": ["A relational database service", "A messaging service", "An object storage service", "A content delivery network service"],
        "answer": "An object storage service"
    },
    {
        "question": "What is the maximum size of an S3 object?",
        "choices": ["5 TB", "10 TB", "15 TB", "20 TB"],
        "answer": "5 TB"
    },
    # add more questions here
]

# Define the quiz route
@app.route('/quiz')
def quiz():
    # Render the quiz template with the first question
    return render_template('quiz.html', question=questions[0]['question'], choices=questions[0]['choices'])

# Define the quiz submission route
@app.route('/quiz', methods=['POST'])
def quiz_submit():
    # Get the selected answer from the form data
    selected_answer = request.form['answer']
    # Get the current question index from the form data
    question_index = int(request.form['question_index'])
    # Get the current question from the questions list
    current_question = questions[question_index]
    # Check if the selected answer is correct
    if selected_answer == current_question['answer']:
        message = "Correct!"
    else:
        message = "Incorrect"
    # If there are more questions, render the next question
    if question_index < len(questions) - 1:
        next_question = questions[question_index + 1]
        return render_template('quiz.html', question=next_question['question'], choices=next_question['choices'], message=message, question_index=question_index + 1)
    # Otherwise, display the results
    else:
        return render_template('quiz_results.html', score=0, total=len(questions))

if __name__ == '__main__':
    app.run(debug=True)


