from login import username, password
import smtplib

def sendEmail():
    sent_from = username
    to = 'lowkhyeean@gmail.com'
    subject = "John Wick 3 is HD!"
    body = "Watch now!\n https://www7.123movies.as/movie/john-wick-chapter-3-parabellum/\n"

    message = "From: %s\r\n" % sent_from + "To: %s\r\n" % to + "Subject: %s\r\n" % subject + "\r\n" + body
    try:
        server = smtplib.SMTP_SSL('smtp.gmail.com', 465)
        server.ehlo()
        server.login(username, password)
        server.sendmail(sent_from, to, message)
        server.close()

        print("Email sent")
    except Exception as e:
        print(e)
