import json
import smtplib, ssl
# Loads wordle answers from words.json
with open("words.json") as fp:
  wordle_answers = json.load(fp)

def spoil():
   # Configures Port
  port = 465
  
  # Grabs login credentials and victim list
  email_ = ""
  password = ""
  victims = []
  with open("credentials.txt", 'r') as fp:
    email_ = fp.readline()
    password = fp.readline()
  with open("victims.txt", 'r') as fp:
    victims = fp.readlines()
  # Grabs the wordle to spoil. 
  try:
    to_spoil = int(input("What wordle would you like to spoil? (EX: 219): "))
  except:
    print("enter a valid wordle to spoil dumbass")
    quit()

  # Create a Secure SSL Context
  context = ssl.create_default_context()

  # Replace the below email with whatever email you are using
  with smtplib.SMTP_SSL("smtp.gmail.com", port, context=context) as server:
    server.login(email_, password)
    for i in range(len(victims)):
      server.sendmail(email_, victims[i], f"Today's wordle answer is {wordle_answers[to_spoil - 1]}.")
      print("Success!")
spoil()
