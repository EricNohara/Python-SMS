# Python-Today's-Workout-SMS-Automated-Sender

## Description:

Python script which makes use of smtplib to send MMS messages to my phone, and pandas library to read data from a public google sheets file with data about my workouts.

## Functionality:

Input: correct email and credentials to send MMS messages from, details about the recipeint phone number and provider, the start date of the workout program, and the days which are lifting days in the program.

Does: sends an MMS message with the day's current workout from the program google sheet. If it is a rest day, sends the message that it is a rest day. Sends an image of a cat lifting a dumbell for bonus motivation.

# Use Instructions:

- Configure a google sheet with the same format provided.
- Make the sheet public access (Share with anyone with the link).
- Copy URL from sheet and replace it with the URLs already in the getsheetdata.py file.
- Replace relavent data in the config.py file.
- Replace values of the day_num_to_lift_num dictionary to reflect the rest and workout days in your program (-1 is a rest day).
- Install pyinstaller (pip install pyinstaller).
- Build your executable file from main.py.
  - Navigate to the working directory of the project, then run on the command line:
  - pyinstaller main.py --onefile
  - Move the main.exe file which is now in the dist folder into the main directory.
- Set up windows task scheduler to run the script daily at a certain time.

## Template Workout Program Format for Google Sheets

https://docs.google.com/spreadsheets/d/1fMjyr4TgCrfVDT1U8fkXCfOyxMf6ulrWpuhltlKi974/edit?usp=sharing

## Demo:

![SMS_sender](https://github.com/EricNohara/Python-SMS-Workout_Sender/assets/123284198/a118151a-2b36-44ab-86a0-91f11b754a60)








