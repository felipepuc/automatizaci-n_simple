from selenium import webdriver
from selenium.webdriver.chrome.options import Options

from funciones_agente.obtener_clima import obtener_clima
from funciones_agente.obtener_precio_accion import obtener_precio_accion
from utils.sanitizar import sanitizar


# Configuración de Google Chrome para Codespaces
options = Options()
options.binary_location = "/usr/bin/google-chrome"

options.add_argument("--headless=new")
options.add_argument("--disable-gpu")
options.add_argument("--no-sandbox")
options.add_argument("--disable-dev-shm-usage")
options.add_argument("--disable-blink-features=AutomationControlled")

# Crear navegador automático
driver = webdriver.Chrome(options=options)


def procesar_input(user_input):
    if "clima" in user_input or "temperatura" in user_input:
        return obtener_clima
    elif "precio" in user_input or "accion" in user_input or "valor" in user_input:
        return obtener_precio_accion
    return None


print("Hola, soy tu asistente virtual. ¿En qué puedo ayudarte hoy?")

try:
    while True:
        user_input = sanitizar(input("---> "))

        if user_input == "salir":
            print("Hasta luego.")
            break

        funcion_agente = procesar_input(user_input)

        if funcion_agente is None:
            print("No entendí tu solicitud. Intenta nuevamente.")
        else:
            respuesta = funcion_agente(driver, user_input)
            print(f">>> {respuesta}")

finally:
    driver.quit()