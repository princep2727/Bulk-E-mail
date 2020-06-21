import pandas as pd
import smtplib
e = pd.read_excel("Email2.xlsx")
emails = e["Emails"].values
server = smtplib.SMTP("smtp.gmail.com", 587)
server.starttls()
server.login("email id here","password here")
msg = "hello this is demo by python"
subject = "Hello world"
body = "Subject: {}\n\n{}".format(subject,msg)
for email in emails:
    server.sendmail("email id here", email, body)
server.quit()