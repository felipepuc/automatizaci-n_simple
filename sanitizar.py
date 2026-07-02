import unicodedata


def sanitizar(texto):
    if texto is None:
        return ""

    texto = texto.lower().strip()
    texto = texto.replace("ñ", "n").replace("ü", "u")

    texto = unicodedata.normalize("NFD", texto)
    texto = "".join(
        caracter for caracter in texto
        if unicodedata.category(caracter) != "Mn"
    )

    signos = ["¿", "?", "¡", "!", ".", ",", ";", ":", '"', "'"]
    for signo in signos:
        texto = texto.replace(signo, "")

    texto = " ".join(texto.split())
    return texto
