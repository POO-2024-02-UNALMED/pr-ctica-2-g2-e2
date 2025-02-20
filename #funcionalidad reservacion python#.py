#funcionalidad reservacion python#
from abc import ABC, abstractmethod
from datetime import datetime, timedelta

class Reservacion(ABC):
    def __init__(self, fecha, hora, personas):
        self._fecha = fecha
        self._hora = hora
        self._personas = personas

    @abstractmethod
    def realizar_reservacion(self):
        pass

    @abstractmethod
    def cancelar_reservacion(self):
        pass

    @abstractmethod
    def aplazar_reservacion(self, nueva_fecha, nueva_hora):
        pass

class ReservacionEstablecimiento(Reservacion):
    def realizar_reservacion(self):
        print(f"Reservación para todo el establecimiento realizada para {self._personas} personas el {self._fecha} a las {self._hora}.")

    def cancelar_reservacion(self):
        print("Reservación para todo el establecimiento cancelada.")

    def aplazar_reservacion(self, nueva_fecha, nueva_hora):
        self._fecha = nueva_fecha
        self._hora = nueva_hora
        print(f"Reservación aplazada a {self._fecha} a las {self._hora}.")

class Mesa:
    def __init__(self, numero, capacidad):
        self.numero = numero
        self.capacidad = capacidad
        self.reservada = False

class ReservacionMesa(Reservacion):
    def __init__(self, fecha, hora, personas, mesa):
        super().__init__(fecha, hora, personas)
        self.mesa = mesa

    def realizar_reservacion(self):
        if not self.mesa.reservada and self.personas <= self.mesa.capacidad:
            self.mesa.reservada = True
            print(f"Reservación para mesa {self.mesa.numero} realizada para {self._personas} personas el {self._fecha} a las {self._hora}.")
        else:
            print("No se puede realizar la reservación. Mesa ya reservada o capacidad insuficiente.")

    def cancelar_reservacion(self):
        self.mesa.reservada = False
        print(f"Reservación para mesa {self.mesa.numero} cancelada.")

    def aplazar_reservacion(self, nueva_fecha, nueva_hora):
        self._fecha = nueva_fecha
        self._hora = nueva_hora
        print(f"Reservación para mesa {self.mesa.numero} aplazada a {self._fecha} a las {self._hora}.")

class Restaurante:
    def __init__(self):
        self.mesas = [Mesa(i, 4) for i in range(1, 11)]  # 10 mesas, cada una con capacidad para 4 personas
        self.reservaciones = []

    def mostrar_mesas(self):
        print("Mesas disponibles:")
        for mesa in self.mesas:
            estado = "Reservada" if mesa.reservada else "Disponible"
            print(f"Mesa {mesa.numero}: Capacidad {mesa.capacidad} - {estado}")

    def realizar_reservacion_establecimiento(self, fecha, hora, personas):
        reservacion = ReservacionEstablecimiento(fecha, hora, personas)
        reservacion.realizar_reservacion()
        self.reservaciones.append(reservacion)

    def realizar_reservacion_mesa(self, fecha, hora, personas, numero_mesa):
        mesa = next((m for m in self.mesas if m.numero == numero_mesa), None)
        if mesa:
            reservacion = ReservacionMesa(fecha, hora, personas, mesa)
            reservacion.realizar_reservacion()
            self.reservaciones.append(reservacion)
        else:
            print("Mesa no encontrada.")

    def cancelar_reservacion(self, reservacion):
        reservacion.cancelar_reservacion()
        self.reservaciones.remove(reservacion)

    def aplazar_reservacion(self, reservacion, nueva_fecha, nueva_hora):
        reservacion.aplazar_reservacion()