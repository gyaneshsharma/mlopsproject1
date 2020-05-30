import smtplib
s = smtplib.SMTP('smtp.gmail.com', 587)
s.starttls()

s.login("gyaneshsharma4@gmail.com", "*************")


#Message that will be sent to mail
msg = "accuracy is achieved"
     
s.sendmail("gyaneshsharma4@gmail.com", "1706221@kiit.ac.in", msg)
    
#For terminating 
s.quit()
