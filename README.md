# Mini Project

  * install Flask 
    sudo pip install flask
    
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

    