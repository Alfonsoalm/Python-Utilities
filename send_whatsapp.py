import pywhatkit
import time

def send_message_whatsapp(number=None, group=None, message=None, hour=None, minute=None):
    try:
        # Verifica si se debe programar el mensaje
        if hour is not None and minute is not None:
            if group:
                pywhatkit.sendwhatmsg_to_group(
                    group_id=group,
                    message=message,
                    time_hour=hour,
                    time_min=minute,
                    wait_time=10,
                    tab_close=True,
                    close_time=5
                )
            elif number:
                pywhatkit.sendwhatmsg(
                    phone_no=number,
                    message=message,
                    time_hour=hour,
                    time_min=minute,
                    wait_time=10,
                    tab_close=True,
                    close_time=5
                )
        else:
            # Enviar inmediatamente
            if group:
                pywhatkit.sendwhatmsg_to_group_instantly(
                    group_id=group,
                    message=message,
                    wait_time=10,
                    tab_close=True,
                    close_time=5
                )
            elif number:
                pywhatkit.sendwhatmsg_instantly(
                    phone_no=number,
                    message=message,
                    wait_time=10,
                    tab_close=True,
                    close_time=5
                )

        print("Mensaje de WhatsApp enviado correctamente!")
    except Exception as e:
        print(f"Ha ocurrido un error al enviar el mensaje de WhatsApp: {e}")

def send_image_whatsapp(numero=None, group=None, imagen=None, mensaje=None, hora=None, minuto=None):
    try:
        # Verifica si se debe enviar a una hora específica
        if hora is not None and minuto is not None:
            if group:
                pywhatkit.sendwhats_image(
                    receiver=group,
                    img_path=imagen,
                    caption=mensaje if mensaje else "",
                    time_hour=hora,
                    time_min=minuto
                )
            elif numero:
                pywhatkit.sendwhats_image(
                    receiver=numero,
                    img_path=imagen,
                    caption=mensaje if mensaje else "",
                    time_hour=hora,
                    time_min=minuto
                )
        else:
            # Enviar inmediatamente si no se especifica hora y minuto
            if group:
                pywhatkit.sendwhats_image(
                    receiver=group,
                    img_path=imagen,
                    caption=mensaje if mensaje else ""
                )
            elif numero:
                pywhatkit.sendwhats_image(
                    receiver=numero,
                    img_path=imagen,
                    caption=mensaje if mensaje else ""
                )

        print("Mensaje de WhatsApp enviado correctamente!")
    except Exception as e:
        print(f"Ha ocurrido un error al enviar el mensaje de WhatsApp: {e}")

if __name__ == "__main__":
    # Enviar mensaje por WhatsApp
    number = 34657289926
    message = "Hola mama, esto es un mensaje automatico"
    try:
        hour = None
        minute = None

        image = "imagen.jpg"
        send_message_whatsapp(number = number, message = message, hour = hour, minute = minute)
        send_image_whatsapp(number = number, image = image, message = message, hour = hour, minute = minute)
    except ValueError:
        print("Por favor, introduce valores válidos para la hora y el minuto (números enteros).")
