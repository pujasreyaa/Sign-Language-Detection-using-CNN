@echo off
echo Deploying to Firebase...

REM Install Firebase CLI
npm install -g firebase-tools

REM Login to Firebase
firebase login

REM Initialize Firebase project
firebase init

REM Deploy to Firebase
firebase deploy

echo Deployment complete!
pause