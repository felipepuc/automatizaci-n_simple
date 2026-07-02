import requests


def extraer_ciudad(texto):
    palabras_a_quitar = [
        "cual es", "la", "el", "actual", "temperatura",
        "clima", "tiempo", "en", "de", "del"
    ]

    ciudad = texto
    for palabra in palabras_a_quitar:
        ciudad = ciudad.replace(palabra, " ")

    ciudad = " ".join(ciudad.split())
    return ciudad


def obtener_clima(texto):
    ciudad = extraer_ciudad(texto)

    if not ciudad:
        return "Indica una ciudad. Ejemplo: clima en Oaxaca."

    try:
        url = f"https://wttr.in/{ciudad}?format=%t"
        respuesta = requests.get(url, timeout=10)

        if respuesta.status_code == 200:
            temperatura = respuesta.text.strip()
            return f"La temperatura actual en {ciudad.title()} es {temperatura}."

        return "No pude obtener el clima de esa ciudad."

    except Exception:
        return "Ocurrió un error al consultar el clima. Revisa tu conexión a internet."
