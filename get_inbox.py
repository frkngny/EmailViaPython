from myinfo import MYMAIL, MYPASSWORD
import imaplib
import email

host = "imap.gmail.com"

blank_mail = {"From": "No one", "To": "-", "Subject": "Oops!", "Body": "There is no unseen mail left!", "Date": "-"}


def get_inbox():
    mail = imaplib.IMAP4_SSL(host)
    mail.login(MYMAIL, MYPASSWORD)
    mail.select('inbox')

    _, searched_data = mail.search(None, 'UNSEEN')

    for searched in searched_data[0].split():
        data_to_return = {}
        _, mail_data = mail.fetch(searched, "(RFC822)")
        _, data = mail_data[0]
        message = email.message_from_bytes(data)

        headers = ["From", "To", "Date", "Subject"]
        for header in headers:
            data_to_return[header] = message[header]

        for msg_part in message.walk():
            if msg_part.get_content_type() == "text/plain":
                data_to_return["Body"] = msg_part.get_payload(decode=False)

        return data_to_return

    return blank_mail


if __name__ == "__main__":
    returned = get_inbox()
    print(returned)