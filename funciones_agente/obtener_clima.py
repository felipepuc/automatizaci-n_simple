import requests


def obtener_clima(user_input):
    ciudad = user_input
    ciudad = ciudad.replace("clima", "")
    ciudad = ciudad.replace("temperatura", "")
    ciudad = ciudad.replace("tiempo", "")
    ciudad = ciudad.replace("en", "")
    ciudad = ciudad.strip()

    if ciudad == "":
        return "Indica una ciudad. Ejemplo: clima en Oaxaca."

    try:
        respuesta = requests.get(f"https://wttr.in/{ciudad}?format=%t", timeout=10)

        if respuesta.status_code == 200:
            temperatura = respuesta.text.strip()
            return f"La temperatura actual en {ciudad.title()} es {temperatura}."

        return "No pude obtener el clima de esa ciudad."

    except Exception:
        return "Ocurrió un error al consultar el clima."
