from main import procesar_input
from utils.sanitizar import sanitizar


def test_sanitizar():
    assert sanitizar("Oaxaca de Juárez") == "oaxaca de juarez"
    assert sanitizar("precio de la acción Microsoft") == "precio de la accion microsoft"
    assert sanitizar("¿Cuál es la temperatura en Ciudad de México?") == "cual es la temperatura en ciudad de mexico"


def test_procesar_input():
    assert procesar_input(sanitizar("clima en Oaxaca")) == "clima"
    assert procesar_input(sanitizar("temperatura en Guadalajara")) == "clima"
    assert procesar_input(sanitizar("precio de la acción Microsoft")) == "precio"
    assert procesar_input(sanitizar("accion apple")) == "precio"
    assert procesar_input(sanitizar("hola")) is None


if __name__ == "__main__":
    test_sanitizar()
    test_procesar_input()
    print("Todas las pruebas pasaron correctamente.")
