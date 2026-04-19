from imapclient import IMAPClient 
import pyzmail


HOST = "imap.gmail.com"
USERNAME = "ayushnikalje121@gmail.com"
PASSWORD = "nytokjolrmzxqxbr"

def read_latest():
    server = IMAPClient(HOST)
    server.login(USERNAME,PASSWORD)
    server.select_folder("INBOX")

    messages = server.search()

    if len(messages) == 0:
        server.logout()
        return None,None
    else:
        last_uid = messages[-1]
        raw_text_content = server.fetch([last_uid],["BODY[]"])

        text_content = pyzmail.PyzMessage.factory(
        raw_text_content[last_uid][b"BODY[]"]
        )

        subject = text_content.get_subject()

        body = text_content.text_part.get_payload().decode(
         text_content.text_part.charset
        )
        server.logout()
        return subject,body

subject, body = read_latest()
print(subject)
print(body)