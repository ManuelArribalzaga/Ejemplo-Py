def saludar(nombre):
    return f"Hola {nombre}, este es un ejemplo de función en Python."

# Nueva función de matemáticas: calcular área de un rectángulo
def area_rectangulo(base, altura):
    return base * altura

if __name__ == "__main__":
    print(saludar("Equipo"))

    # Probando la función de área
    base = 5
    altura = 3
    print(f"El área del rectángulo de base {base} y altura {altura} es {area_rectangulo(base, altura)}")
