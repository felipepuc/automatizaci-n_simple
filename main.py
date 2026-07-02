from funciones_agente.obtener_clima import obtener_clima
from funciones_agente.obtener_precio_accion import obtener_precio_accion
from utilidades.sanitizar import sanitizar


def procesar_input(texto):
    palabras_clima = ["clima", "temperatura", "tiempo"]
    palabras_precio = ["precio", "accion", "acciones", "stock", "cotizacion", "valor"]

    if any(palabra in texto for palabra in palabras_clima):
        return "clima"

    if any(palabra in texto for palabra in palabras_precio):
        return "precio"

    return None


def chatbot():
    print("*** Chatbot v1.0.0***")
    print("Hola, soy el Chatbot v1.0.0. Puedo ayudarte a obtener precios de acciones")
    print("o indicarte la temperatura actual en cualquier ciudad del mundo.")
    print("Puedes escribir ejemplos como:")
    print("precio de la acción de Microsoft")
    print("clima en Oaxaca")
    print("Escribe salir para terminar.\n")

    while True:
        user_input = sanitizar(input("--> "))

        if user_input in ["salir", "exit", "quit", "adios"]:
            print(">>> Gracias por usar el chatbot. Hasta luego.")
            break

        intencion = procesar_input(user_input)

        if intencion == "clima":
            print(">>> " + obtener_clima(user_input))

        elif intencion == "precio":
            print(">>> " + obtener_precio_accion(user_input))

        else:
            print(">>> No entendí tu solicitud. Pregúntame por el clima o por el precio de una acción.")


if __name__ == "__main__":
    chatbot()
