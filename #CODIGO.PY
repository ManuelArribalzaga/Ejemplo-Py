def saludar(nombre, mensaje="que tengas un buen día"):
    if not isinstance(nombre, str):
        return "Error: El nombre proporcionado debe ser una cadena de texto."

    return f"Hola {nombre}, {mensaje}. Este es un ejemplo de función en Python."

if _name_ == "_main_":
    print(saludar("Equipo"))
    print(saludar("Ana", "bienvenida al proyecto"))

    nombres = ["Carlos", "Sofía", "Luis"]
    for persona in nombres:
        print(saludar(persona))

    print(saludar(123))
