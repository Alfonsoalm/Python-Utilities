import imaplib
import email
from email.header import decode_header
from credentials import username, password  # Importar credenciales

def read_emails(username, password):
    try:
        # Conectarse al servidor de Gmail
        imap = imaplib.IMAP4_SSL("imap.gmail.com")

        # Iniciar sesión en la cuenta
        imap.login(username, password)

        # Seleccionar la bandeja de entrada
        imap.select("inbox")

        # Buscar correos electrónicos (todos los correos)
        status, messages = imap.search(None, "ALL")

        # Convertir los resultados en una lista de IDs de mensajes
        mail_ids = messages[0].split()

        print(f"Se encontraron {len(mail_ids)} correos electrónicos.")

        # Leer los últimos 10 correos electrónicos
        for i in mail_ids[-10:]:
            # Fetch del correo electrónico por su ID
            res, msg = imap.fetch(i, "(RFC822)")

            for response in msg:
                if isinstance(response, tuple):
                    # Parsear el contenido del mensaje
                    msg = email.message_from_bytes(response[1])

                    # Obtener el asunto del correo
                    subject, encoding = decode_header(msg["Subject"])[0]
                    if isinstance(subject, bytes):
                        # Si el asunto está codificado en bytes, decodificarlo
                        subject = subject.decode(encoding if encoding else "utf-8")

                    # Obtener el remitente
                    from_ = msg.get("From")

                    # Obtener la fecha
                    date = msg.get("Date")

                    print(f"De: {from_}")
                    print(f"Asunto: {subject}")
                    print(f"Fecha: {date}")
                    print("-" * 50)

        # Cerrar la conexión y cerrar sesión
        imap.close()
        imap.logout()

    except Exception as e:
        print(f"Error: {e}")

if __name__ == "__main__":
    read_emails(username, password)
