# Mini Project

  * install Flask 
    sudo pip3 install flask
    
  * Basic python needed:
    import os
from flask import Flask

app = Flask(__name__)

#forward slash refers to default route
@app.route("/")
def hello():
    return 'Hello World ...again'
    
if __name__ == '__main__':
    app.run(host=os.environ.get('IP'),
            port=int(os.environ.get('PORT')),
            debug=True),


  * Next, create an app in Heroku (app project name must be unique)
  * Then log into Heroku via cloud9 bash "Heroku Login" then enter email and password
  * "heroku apps" bash command lets you see what apps you have with heroku
  * then git init
  * copy and paste the link in the heroku website "heroku git:remote -a task-manager-flask-mongo-joc" to set git heroku remote. 
  * You can't push to Heroku without a requirements.txt file. Use the below command in bash to do that. 
  * sudo pip3 freeze --local > requirements.txt
  * then git commit again
  * then push to heroku "git push heroku master"
  * Next, add a procfile:
  * echo web: python app.py > Procfile
  * Git commit "added Procfile" and push to heroku again
  * Next we want to run our application, enter the following into bash:
  * heroku ps:scale web=1
  * Dynos are scaled with this command
  * go to heroku and go to settings, and reveal and config vVars
  * Enter IP and set value to 0.0.0.0   Enter PORT as the next key and enter 5000 as key
    