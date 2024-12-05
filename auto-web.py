from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import pandas as pd
from datetime import datetime
import os
import sys

aplication_path = os.path.dirname(sys.executable)
time_now = datetime.now()
formated_date = time_now.strftime("%m%d%Y")


# URL del sitio web
website = "https://lms.santanderopenacademy.com/courses/373/pages/chapter-5-the-apple"

# Ruta al archivo ejecutable de ChromeDriver
path = "C:/Users/ant45/OneDrive/Escritorio/INSTALADORES/chromedriver-win64/chromedriver-win64/chromedriver.exe"


# Configuración en modo headless
options = Options()
options.add_argument("--headless")
options.add_argument("--disable-gpu")
options.add_argument("--no-sandbox")
options.add_argument("--disable-dev-shm-usage")

# Configuración del servicio de Selenium
service = Service(executable_path=path)
driver = webdriver.Chrome(service=service, options=options)
driver.get(website)

# Imprimir el DOM inicial de la página para depuración
print("HTML inicial:")
print(driver.page_source)
try:
    # Abrir la página de inicio de sesión
    driver.get(website)

    # Completar el campo de usuario (email)
    WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.ID, "username"))
    )
    username_field = driver.find_element(By.ID, "username")
    username_field.send_keys("alfonsoalm34@gmail.com")  # Cambia por tu email

    # Completar el campo de contraseña
    password_field = driver.find_element(By.ID, "password")
    password_field.send_keys("Nasimientomininio1410%")  # Cambia por tu contraseña

    # Hacer clic en el botón de inicio de sesión
    login_button = driver.find_element(By.ID, "kc-login")
    login_button.click()

    # Esperar a que la página se cargue después del inicio de sesión
    WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.XPATH, '//div[@class="show-content user_content clearfix enhanced"]'))
    )

    # Continuar con el scraping después de iniciar sesión
    container = driver.find_element(By.XPATH, '//div[@class="show-content user_content clearfix enhanced"]')
    text_content = container.find_element(By.XPATH, './div/div/details/div/p').text

    print("Contenido extraído:", text_content)

    # Guardar los datos en un archivo CSV
    data = {'Content': [text_content]}
    df = pd.DataFrame(data)
    df.to_csv(output_file, index=False)
    print(f"Archivo {output_file} generado con éxito.")

except Exception as e:
    print("Error durante la ejecución:", e)

finally:
    # Cerrar el navegador
    driver.quit()