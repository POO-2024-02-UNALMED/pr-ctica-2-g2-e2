def entrada():
    x = False
    while (x == False):
        try:
            cedula = int(input())
        except ValueError:
            print("Error de entrada, por favor ingrese un número")
            continue
        x = True
    return cedula

def ingresarNombre():
    x = False
    while x == False:
        nombre = input()
        if "1" in nombre or "2" in nombre or "3" in nombre or "4" in nombre or "5" in nombre or "6" in nombre or "7" in nombre or "8" in nombre or "9" in nombre or "0" in nombre or "_" in nombre or "," in nombre or "-" in nombre or "." in nombre:
            print("Caracter no permitido, ingrese únicamente letras")
            continue
        x = True
    return nombre
