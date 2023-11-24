import imaplib
import email as em
from time import sleep


def get_twitter_code(email: str, password: str) -> str:
    sleep(4)
    codes = []
    imap_server = "outlook.office365.com"
    if "hotmail" in email:
        imap_server = "imap-mail.outlook.com"
    mail = imaplib.IMAP4_SSL(imap_server)
    mail.login(email, password)
    mail.select('inbox')
    status, data = mail.search(None, '(ALL)')

    for num in data[0].split()[::-1]:
        status, data = mail.fetch(num, '(RFC822)')
        email_message = em.message_from_bytes(data[0][1])
        if "Twitter" in str(email_message['From']) and "confirmation code" in str(email_message['Subject']):
            subj = str(email_message['Subject'])
            mail.close()
            mail.logout()
            return subj.split(' ')[-1]

    mail.close()
    mail.logout()
    return codes[-1]
