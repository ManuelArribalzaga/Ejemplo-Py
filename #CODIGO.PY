def saludar(grupo):

    return f"¡Hola {grupo}! Bienvenidos a la clase de Herramientas de Software en la Nube."


def motivar(grupo):
   
    return f"{grupo}, recuerden: cada línea de código los acerca más a sus metas."


def despedir(grupo):
   
    return f"Adiós {grupo}, sigan practicando y aprendiendo cada día. ¡Nos vemos pronto!"


def agradecimiento(nombre):
   
    return f"Gracias por tu esfuerzo, {nombre}. ¡Tu dedicación marca la diferencia! "


if __name__ == "__main__":
    grupo = "Grupo de Herramientas"
    integrante = "Aurora"

    print(saludar(grupo))
    print(motivar(grupo))
    print(agradecimiento(integrante))
    print(despedir(grupo))
