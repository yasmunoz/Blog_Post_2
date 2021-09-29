'''
In this example, we are going to look at creating, serving, and deploying a *very simple* webapp. In the following several lectures, we'll see how to add some interesting interactivity to our app. 

# Prerequisites

- You need to have the flask package installed in your PIC16B Anaconda environment. 
- You need a Heroku account. 
- At the command line, run 
    conda activate PIC16B
    
# Sources

This set of lecture notes is based in part on previous materials developed by Erin George (UCLA Mathematics) and the tutorial [here](https://stackabuse.com/deploying-a-flask-application-to-heroku/). 
'''


from flask import Flask, render_template, request
app = Flask(__name__)

@app.route("/")

# simplest possible approach
# def main():
#     return "hi there!"


# slightly less trivial
# def main():
#     return render_template("main.html")

# fancier template
@app.route("/")
def main():
    return render_template("main_better.html")
