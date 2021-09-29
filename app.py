'''
In this example, we are going to look at creating, serving, and deploying a *very simple* webapp. In the following several lectures, we'll see how to add some interesting interactivity to our app. 

# Prerequisites

- You need to have the flask package installed in your PIC16B Anaconda environment. 
- You need a Heroku account.
- You need the Heroku command line interface: 
    - At the command line:
    brew tap heroku/brew && brew install heroku

- At the command line, run 
    conda activate PIC16B

# Deployment

*Note*: these notes are written for the version of the app that Phil is using, which is indeed called pic16b-minimal-demo. In order to make your own version, you would need to give the app a different name (because one with this name already exists now).

Sign up for Heroku, create app called pic16b-minimal-demo

```
heroku login
heroku git:remote -a pic16b-minimal-demo

git add *.
git commit -m'add files for heroku'
git push heroku
```

Then, website is at 
https://pic16b-minimal-demo.herokuapp.com

This URL 
    
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
