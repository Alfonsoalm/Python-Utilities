import pywhatkit
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.options import Options
import time


def read_last_messages(contact_name, num_messages):
    # Configurar Chrome para usar el perfil existente
    chrome_options = Options()
    chrome_options.add_argument(r"user-data-dir=C:\Users\CTM40\AppData\Local\Google\Chrome\User Data")
    chrome_options.add_argument("--profile-directory=Default")  # Usa el perfil "Default"

    # Crear el navegador con las opciones
    driver = webdriver.Chrome(options=chrome_options)
    driver.get("https://web.whatsapp.com/")

    print("Escanea el código QR para iniciar sesión en WhatsApp Web.")
    time.sleep(5)  # Esperar a que el usuario inicie sesión

    # Buscar el contacto
    search_box = driver.find_element(By.XPATH, "//div[@contenteditable='true']")
    search_box.click()
    search_box.send_keys(contact_name)
    search_box.send_keys(Keys.ENTER)
    time.sleep(3)

    # Buscar mensajes en el chat
    messages = driver.find_elements(By.XPATH, "//div[contains(@class, 'message-in') or contains(@class, 'message-out')]")
    last_messages = messages[-num_messages:]  # Obtener los últimos 'n' mensajes

    # Abrir archivo para guardar mensajes
    file_name = f"{contact_name}_last_messages.txt"
    with open(file_name, "w", encoding="utf-8") as file:
        for message in last_messages:
            try:
                text_element = message.find_element(By.XPATH, './div/div/div/div/div/div//span[@class="_ao3e selectable-text copyable-text"]')
                text = text_element.text
                
                if 'message-in' in message.get_attribute("class"):
                    # Mensaje del contacto
                    file.write(f"{contact_name}: {text}\n")
                elif 'message-out' in message.get_attribute("class"):
                    # Mensaje tuyo
                    file.write(f"Tú: {text}\n")
            except Exception as e:
                print(f"Error al leer el mensaje: {e}")

    print(f"Mensajes guardados en el archivo: {file_name}")
    driver.quit()


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
        # hour = None
        # minute = None
        # image = "imagen.jpg"
        # send_message_whatsapp(number = number, message = message, hour = hour, minute = minute)
        # send_image_whatsapp(number = number, image = image, message = message, hour = hour, minute = minute)
        contact = "Antonia"
        n = 5
        read_last_messages(contact, n)

    except ValueError:
        print("Por favor, introduce valores válidos para la hora y el minuto (números enteros).")
