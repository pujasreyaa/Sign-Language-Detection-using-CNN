@echo off
echo Deploying Sign Language Detection App...

REM Install Heroku CLI first from https://devcenter.heroku.com/articles/heroku-cli

echo 1. Login to Heroku
heroku login

echo 2. Create Heroku app
heroku create your-asl-app-name

echo 3. Set buildpack
heroku buildpacks:set heroku/python

echo 4. Initialize git and deploy
git init
git add .
git commit -m "Initial deployment"
git push heroku main

echo 5. Open app
heroku open

pause