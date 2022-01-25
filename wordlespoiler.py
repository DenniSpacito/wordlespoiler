import json
import smtplib, ssl
# Loads wordle answers from words.json
with open("words.json") as fp:
  wordle_answers = json.load(fp)

# Configures Port
port = 465
 

# email, password, reciever email, message
email_ = input("Enter your email: ")
password = input("Enter your email's password: ")
reciever_email = input("What is the email of the person you are emailing?: ")
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
  server.sendmail(email_, reciever_email, f"Today's wordle answer is {wordle_answers[to_spoil]}")
