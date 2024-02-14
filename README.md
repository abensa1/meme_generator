# Meme Generator
## Overview
Flask aplication that generates memes from uploaded images. 

## Local Venv Deployment
1. Set up a python virtual env with the following command:
``python3 -m venv venv_name``
2. Install all the dependencies by running ``pip install -r requirements.txt``
3. Set up the main app as the flask variable ``export FLASK_APP=app.py``
4. Run the flask command ``flask run --host localhost --port 3000``
5. Open ``localhost:3000`` in a new browser tab

## Herkou Deployment
1. gunicorn package and Procfile are already set up
2. Create a Herkou account
3. Install Herkou CLI by following the steps outline on https://devcenter.heroku.com/articles/heroku-cli
4. Log in to Heroku via CLI by running ``herkou login``
5. Create Heroku app by running ``heroku create <app name>``
6. Deploy git branch to Heroku by running ``git push heroku <git branch name>``

    If you're experiancing trouble, check this youtube video https://www.youtube.com/watch?v=D2GLVoiEZyE&t=228s

