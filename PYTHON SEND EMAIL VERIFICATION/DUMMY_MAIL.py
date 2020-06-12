import smtplib
# =============================================================================
# SET EMAIL LOGIN REQUIREMENTS
# =============================================================================

#Give Access TO Less Secure App First Then This work otherwise you will problems
# https://www.google.com/settings/security/lesssecureapps
# copy this to the browser and give the access.

gmail_user = "dummy_id@gmail.com"
gmail_app_password = "dummy_pd"

# =============================================================================
# SET THE INFO ABOUT THE SAID EMAIL
# =============================================================================
sent_from = gmail_user
sent_to = ['dummy_receiver@gmail.com']
sent_subject = "Email Verification Checking"
sent_body = ("NACHO RE...!!!\n\n"
             "AYA RE BABA!\n"
             "\n"
             "DARU LA RE...!!\n"
             "YEEE....!!!!\n")

email_text = """\
From: %s
To: %s
Subject: %s

%s
""" % (sent_from, ", ".join(sent_to), sent_subject, sent_body)

try:
    
    server = smtplib.SMTP("smtp.gmail.com", 587)
    server.starttls()
    server.login(gmail_user, gmail_app_password)
    server.sendmail(sent_from, sent_to, email_text)
    server.close()
    print('Email sent!')
except Exception as exception:
    print("Error: %s!\n\n" % exception)