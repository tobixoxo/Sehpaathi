from flask import Flask, render_template, request
app = Flask(__name__)

CHAT_HISTORY = []
@app.route('/', methods = ['POST', 'GET'])
def hello():
    if request.method == 'POST':
        student_query = request.form['query']
        if student_query == "":
            return
        bot_response = "This is dummy Response!"
        # print("Query is : ", bot_response)
        CHAT_HISTORY.append(student_query)
        CHAT_HISTORY.append(bot_response)
        return render_template('chatbot.html',CHAT_HISTORY = CHAT_HISTORY)
    return render_template('chatbot.html')