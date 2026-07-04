import yfinance as yf
from utils.sanitizar import sanitizar

EMPRESAS = {
    "microsoft": "MSFT",
    "apple": "AAPL",
    "google": "GOOGL",
    "alphabet": "GOOGL",
    "amazon": "AMZN",
    "tesla": "TSLA",
    "meta": "META",
    "facebook": "META",
    "netflix": "NFLX",
    "nvidia": "NVDA"
}

def obtener_precio_accion(driver, consulta):
    consulta = sanitizar(consulta)

    ticker = None
    empresa_encontrada = None

    for empresa, simbolo in EMPRESAS.items():
        if empresa in consulta:
            ticker = simbolo
            empresa_encontrada = empresa
            break

    if ticker is None:
        return "No encontré la empresa solicitada. Intenta con Apple, Microsoft, Tesla, Amazon, Google, Meta, Netflix o Nvidia."

    try:
        accion = yf.Ticker(ticker)

        historial = accion.history(period="5d")

        if historial.empty:
            return f"No pude obtener el precio actual de {empresa_encontrada}."

        precio = historial["Close"].iloc[-1]

        try:
            divisa = accion.fast_info.get("currency", "USD")
        except Exception:
            divisa = "USD"

        return f"El precio actual de la acción de {empresa_encontrada.title()} ({ticker}) es {precio:.2f} {divisa}."

    except Exception as error:
        return f"Ocurrió un error al obtener el precio de la acción: {error}"