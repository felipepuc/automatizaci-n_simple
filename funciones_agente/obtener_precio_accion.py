import yfinance as yf


EMPRESAS = {
    "microsoft": "MSFT",
    "apple": "AAPL",
    "tesla": "TSLA",
    "google": "GOOGL",
    "amazon": "AMZN",
    "meta": "META",
    "netflix": "NFLX",
    "nvidia": "NVDA"
}


def obtener_precio_accion(user_input):
    empresa = user_input
    empresa = empresa.replace("precio", "")
    empresa = empresa.replace("accion", "")
    empresa = empresa.replace("acciones", "")
    empresa = empresa.replace("stock", "")
    empresa = empresa.replace("cotizacion", "")
    empresa = empresa.replace("valor", "")
    empresa = empresa.replace("de", "")
    empresa = empresa.replace("la", "")
    empresa = empresa.strip()

    if empresa == "":
        return "Indica una empresa. Ejemplo: precio de la acción Microsoft."

    ticker = EMPRESAS.get(empresa, empresa.upper())

    try:
        accion = yf.Ticker(ticker)
        datos = accion.history(period="1d")

        if datos.empty:
            return f"No encontré datos para {empresa.title()}."

        precio = datos["Close"].iloc[-1]
        return f"El precio actual de la acción de {empresa.title()} es ${precio:.2f}."

    except Exception:
        return "Ocurrió un error al consultar el precio de la acción."
