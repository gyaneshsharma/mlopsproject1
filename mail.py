import smtplib
s = smtplib.SMTP('smtp.gmail.com', 587)
s.starttls()

s.login("anshulmishra654@gmail.com", "*************")


#Message that will be sent to mail
msg = "accuracy is less than 90%.Try again"
     
s.sendmail("anshulmishra654@gmail.com", "1706205@kiit.ac.in", msg)
    
#For terminating 
s.quit()
