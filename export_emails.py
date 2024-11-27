import imaplib
import email
from email.header import decode_header
import json

# Leer credenciales desde config.json
with open("data.json") as f:
    config = json.load(f)

username = config["email"]
password = config["password"]

# Función para iniciar sesión en el correo
def login_email(username, password, server="imap.gmail.com"):
    mail = imaplib.IMAP4_SSL(server)
    mail.login(username, password)
    return mail

# Función para leer correos electrónicos
def read_emails(mail, folder="inbox"):
    mail.select(folder)
    status, messages = mail.search(None, "ALL")
    email_ids = messages[0].split()
    emails = []
    for email_id in email_ids[-10:]:  # Leer los últimos 10 correos
        status, msg_data = mail.fetch(email_id, "(RFC822)")
        for response_part in msg_data:
            if isinstance(response_part, tuple):
                msg = email.message_from_bytes(response_part[1])
                subject = decode_header(msg["Subject"])[0][0]
                if isinstance(subject, bytes):
                    subject = subject.decode()
                emails.append({"subject": subject, "body": get_email_body(msg)})
    return emails

# Extraer el cuerpo del correo
def get_email_body(msg):
    if msg.is_multipart():
        for part in msg.walk():
            if part.get_content_type() == "text/plain":
                return part.get_payload(decode=True).decode()
    else:
        return msg.get_payload(decode=True).decode()

# Conectar y leer correos
mail = login_email(username, password)
emails = read_emails(mail)
mail.logout()

print(emails)
