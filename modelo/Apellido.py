from enum import Enum

class Apellido(Enum):
    Rodríguez = 1
    Martínez = 2
    García = 3
    Gómez = 4
    López = 5
    González = 6
    Hernández = 7
    Sánchez = 8
    Pérez = 9
    Ramírez = 10
    Díaz = 11
    Torres = 12
    Muñoz = 13
    Rojas = 14
    Moreno = 15
    Vargas = 16
    Ortiz = 17
    Jiménez = 18
    Castro = 19
    GUtiérrez = 20
    Álvarez = 21
    Valencia = 22
    Ruiz = 23
    SUárez = 24
    Herrera = 25
    Borja = 26
    Caicedo = 27
    León = 28
    Bernal = 29
    loaiza = 30
    Cano = 31
    Castillo = 32
    Franco = 33
    Miranda = 34
    Mosquera = 35
    Murillo = 36
    Andrade = 37
    Villa = 38
    Montero = 39
    Palacios = 40
    Flórez = 41
    Blanco = 42
    Ramos = 43
    Rincón = 44
    Madrid = 45
    Castaño = 46
    Pardo = 47
    Galarga = 48
    Camela = 49
    Nito = 50
    Rubio = 51
    Ríos = 52
    Martín = 53
    Giraldo = 54
    Guerra = 55
    Restrepo = 56
    Zuluaga = 57
    Duque = 58
    Uribe = 59
    Petro = 60
    Hoyos = 61
    Fernández = 62
    Garro = 63
    Cabal = 64
    Pineda = 65
    Melano = 66
    Duarte = 67
    Pedroza = 68
    Parra = 69
    Rendón = 70

    @staticmethod
    def getNombre(id):
        for nombre in Apellido:
            if nombre.value == id:
                return nombre.name
        return "Guzmán"