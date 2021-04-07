import smtplib
import ssl
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText


def mail_sender():
    port = 465
    password = "*****"
    mymail = "robotautomatanotif@gmail.com"
    recmail = ["ielyazov2@gmail.com"]

    message = MIMEMultipart("alternative")
    message["Subject"] = 0
    message["From"] = mymail
    message["To"] = recmail

    text = """"""

    html = ("\\n"
            "    <html>\n"
            "      <body>\n"
            "        <p>\n"
            "        \"You have a new notification from {} at the date of {} \"\n"
            "        </p>\n"
            "      </body>\n"
            "    </html>\n"
            "    ").format()

    part1 = MIMEText(text, "plain")
    part2 = MIMEText(html, "html")

    message.attach(part1)
    message.attach(part2)

    context = ssl.create_default_context()
    with smtplib.SMTP_SSL("smtp.gmail.com", port, context=context) as server:
        server.login(mymail, password)
        server.sendmail(mymail, recmail, message.as_string())
        print("Message sent!")
