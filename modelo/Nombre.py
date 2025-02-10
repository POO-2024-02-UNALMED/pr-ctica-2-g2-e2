from enum import Enum

class Nombre(Enum):
    Esteban = 1
    Sergio = 2
    Andrés = 3
    Antonio = 4
    Marcos = 5
    Rubén = 6
    David = 7
    Jesús = 8
    Fernando = 9
    Daniel = 10
    Daniela = 11
    Camila = 12
    María = 13
    Julia = 14
    Carmen = 15
    Santiago = 16
    Pablo = 17
    Paulina = 18
    Rosa = 19
    Alejandra = 20
    Víctor = 21
    Manuela = 22
    Manuel = 23
    Mateo = 24
    Luis = 25
    Valentina = 26
    Valeria = 27
    Ánderson = 28
    Eugenio = 29
    Rodrigo = 30
    Mariana = 31
    Catalina = 32
    José = 33
    Carlos = 34
    Hernando = 35
    Martín = 36
    Ángela = 37
    Edna = 38
    Bryan = 39
    Ximena = 40
    Sara = 41
    Estela = 42
    Elena = 43
    Elver = 44
    Diego = 45
    Marta = 46
    Gloria = 47
    Diana = 48
    Luisa = 49
    Sandra = 50
    Alexander = 51
    Emiliano = 52
    Juan = 53
    Joaquín = 54
    Verónica = 55
    Roberto = 56
    Ricardo = 57
    Sebastián = 58
    Ana = 59
    Laura = 60
    Roxana = 61
    Jacobo = 62
    Raúl = 63
    Gustavo = 64
    Luciana = 65
    Gerardo = 66
    Guillermo = 67
    Francisco = 68
    Benito = 69
    Susana = 70

    @staticmethod
    def getNombre(id):
        for nombre in Nombre:
            if nombre.value == id:
                return nombre.name
        return "Jaime"