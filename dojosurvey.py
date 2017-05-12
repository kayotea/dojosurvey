from flask import Flask, request, render_template
app = Flask(__name__)

@app.route('/')
def index():
    return render_template('dojosurvey.html')

@app.route('/submit', methods=["POST"])
def right():
    name = request.form['name']
    location = request.form['location']
    lang = request.form['language']
    comment = request.form['comment']

    return render_template('submit.html', name=name, location=location, lang=lang, comment=comment)

app.run(debug = True)