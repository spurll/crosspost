from email.mime.text import MIMEText
from smtplib import SMTP


SMTPHOST = 'smtp.gmail.com:587'


class Mailbox:
    """
    Sends emails (based on MailTrigger, written by bcj for Polly).
    """

    def __init__(self, username=None, password=None, host=SMTPHOST, bcc=False):
        self.username = username
        self.password = password
        self.bcc = bcc
        self.host = host
        self.smtp = None

    def connect(self):
        self.smtp = SMTP(self.host)
        self.smtp.starttls()
        self.smtp.login(self.username, self.password)

    def disconnect(self):
        self.smtp.close()

    def send(self, recipients, body, subject, bcc=None):
        if bcc is None: bcc = self.bcc

        # Build message.
        message = MIMEText(body)
        message['subject'] = subject
        if not bcc:
            message['to'] = ', '.join(recipients)
        message = message.as_string()

        # Send message.
        self.connect()
        if bcc:
            for recipient in recipients:
                self.smtp.sendmail(self.username, [recipient], message)
        else:
            self.smtp.sendmail(self.username, recipients, message)
        self.disconnect()

