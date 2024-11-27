import pywhatkit
import time

def enviar_mensaje_whatsapp(numero, mensaje, hora, minuto):
    try:
        pywhatkit.sendwhatmsg(numero, mensaje, hora, minuto, 10, True, 5)
        print("Mensaje de WhatsApp enviado correctamente!")
    except Exception as e:
        print(f"Ha ocurrido un error al enviar el mensaje de WhatsApp: {e}")

if __name__ == "__main__":
    # Enviar mensaje por WhatsApp
    numero = input("Introduce el número de teléfono (con código de país, por ejemplo +34 para España): ")
    mensaje = input("Introduce el mensaje a enviar: ")
    try:
        hora = int(input("Introduce la hora de envío (formato 24h, de 0 a 23): "))
        minuto = int(input("Introduce el minuto de envío (de 0 a 59): "))
        enviar_mensaje_whatsapp(numero, mensaje, hora, minuto)
    except ValueError:
        print("Por favor, introduce valores válidos para la hora y el minuto (números enteros).")
