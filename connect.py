import imaplib
import email
import os

imap_server = "imap.gmail.com"
email_address = "sentiment.tester@gmail.com"
password = "smyv zhms bdol hdus"  

imap = imaplib.IMAP4_SSL(imap_server)
imap.login(email_address, password)

imap.select("Inbox")

status, msgnums = imap.search(None, "ALL")

msgnums = msgnums[0].split()

with open('content.txt', 'r+') as f:
        f.truncate(0)

for msgnum in msgnums:
    status, data = imap.fetch(msgnum, "(RFC822)")
    raw_email = data[0][1]
    message = email.message_from_bytes(raw_email)

    with open("content.txt", "a") as file:
        file.write(f"From: {message.get('From')}\n")
        file.write(f"To: {message.get('To')}\n")
        file.write(f"Date: {message.get('Date')}\n")
        file.write(f"BCC: {message.get('BCC')}\n")
        file.write("Content:\n")
        
        for part in message.walk():
            if part.get_content_type() == "text/plain":
                file.write(part.get_payload(decode=True).decode('utf-8'))
        file.write("\n\n") 

print(f"{os.getcwd()}{os.sep}content.txt")

imap.close()
imap.logout()
    
    

