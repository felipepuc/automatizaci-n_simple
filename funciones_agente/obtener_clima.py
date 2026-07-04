from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from urllib.parse import quote_plus


def obtener_clima(driver, consulta):
    consulta = consulta.replace("clima", "")
    consulta = consulta.replace("temperatura", "")
    consulta = consulta.strip()

    if consulta == "":
        return "Por favor, indica la ciudad. Ejemplo: clima Chetumal"

    try:
        busqueda = quote_plus(f"clima {consulta}")
        driver.get(f"https://www.google.com/search?q={busqueda}&hl=es&gl=mx")

        espera = WebDriverWait(driver, 15)

        temperatura = espera.until(
            EC.presence_of_element_located((By.ID, "wob_tm"))
        ).text

        ubicacion = driver.find_element(By.ID, "wob_loc").text
        condicion = driver.find_element(By.ID, "wob_dc").text

        try:
            humedad = driver.find_element(By.ID, "wob_hm").text
        except Exception:
            humedad = "No disponible"

        try:
            viento = driver.find_element(By.ID, "wob_ws").text
        except Exception:
            viento = "No disponible"

        return f"El clima en {ubicacion} es de {temperatura}°C, con condición: {condicion}. Humedad: {humedad}. Viento: {viento}."

    except Exception:
        return f"No pude obtener el clima de {consulta}. Google puede estar bloqueando la búsqueda automática."