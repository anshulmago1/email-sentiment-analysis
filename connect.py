import imaplib
import email

imap_server = "imap.gmail.com"
email_address = "sentiment.tester@gmail.com"
password = "smyv zhms bdol hdus"

imap = imaplib.IMAP4_SSL(imap_server)
imap.login(email_address, password)

imap.select("Inbox")

_, msgnums = imap.search(None, "ALL")

for msgnums in msgnums[0].split():
    _, data = imap.fetch(msgnums, "(RFC822)")

    message = email.message_from_bytes(data[0][1])
    
   
    print(f"From: {message.get('From')}")
    print(f"To: {message.get('To')}")
    print(f"BCC: {message.get('BCC')}")
    print(f"Date: {message.get('Date')}")
    print(f"Subject: {message.get('Subject')}")
    
    print("Content:")
    
    for part in message.walk():
        if part.get_content_type() == "text/plain":
            print(part.as_string())

imap.close()
    
    
    

