def saludar(nombre):
    return f"Hola {nombre}, este es un ejemplo de función en Python."

# NUEVA FUNCIÓN 
def dividir(a, b):
    if b == 0:
        return "Error: División por cero"
    return a / b

if __name__ == "__main__":
    print(saludar("Equipo"))
    print(f"El resultado de la división es: {dividir(10, 2)}")