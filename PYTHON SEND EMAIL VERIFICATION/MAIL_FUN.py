import smtplib
 
def sendemail(from_addr, to_addr_list, cc_addr_list,
              subject, message,
              login, password,
              smtpserver='smtp.gmail.com:587'):
    
    server = smtplib.SMTP(smtpserver)
    server.starttls()
    server.login(login,password)
    server.sendmail(from_addr, to_addr_list, message)
    server.quit()
    
sendemail(from_addr    = 'pratikmahobiya18@gmail.com', 
          to_addr_list = ['prashant.20173@gmail.com'],
          cc_addr_list = ['RC@xx.co.uk'], 
          subject      = 'Howdy', 
          message      = 'Abee AAgya Re..', 
          login        = "prashant.20173@gmail.com", 
          password     = "prashant173")