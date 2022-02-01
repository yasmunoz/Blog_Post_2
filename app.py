from flask import Flask, render_template, request
app = Flask(__name__)

@app.route("/")
def main():
    return render_template('base.html')

@app.route("/view/", methods=['POST', 'GET'])
def view():
    return render_template('ask.html', methods=['POST', 'GET'])
@app.route("/submit/")
def submit():
    return render_template('submit.html')
