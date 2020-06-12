import smtplib


smtpserver = smtplib.SMTP("smtp.gmail.com", 587)
smtpserver.ehlo()
smtpserver.starttls()
smtpserver.ehlo()
smtpserver.login("prashant.20173@gmail.com", "prashant173")
msg='AAYA NA MAIL.. BOL AYA NA..'
smtpserver.sendmail("prashant.20173@gmail.com", "@gmail.com", msg)
print(Mail sent...)