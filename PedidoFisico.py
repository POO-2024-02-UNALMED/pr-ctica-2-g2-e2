from OrdenFisica import OrdenFisica
from entrada import entrada
class PedidoFisico(OrdenFisica):
    def __init__(self, mesa, cliente, mesero, sucursal, numero, chef, pedido):
        super().__init__(mesa, cliente, mesero, sucursal)
        self.numeroDePersonas = numero
        self.chef = chef
        self.pedido = pedido
    
    def getNumeroDePersonas(self): return self.numeroDePersonas

    def getChef(self): return self.chef

    def getPedido(self): return self.pedido
    
    def facturacion(self):
        precio = 0
        i = 0
        for plato in self.pedido:
            if i == 0:
                platos = plato.getNombre() + ": $" + str(plato.getPrecio()) + "\n"
            else:
                platos = platos + plato.getNombre() + ": $" +str(plato.getPrecio()) + "\n"
            precio += plato.getPrecio()
            i += 1
        
        descuento = 0
        if precio <= 20000:
            self.CLIENTE.sumar_puntos(1)
        elif precio <= 100000:
            self.CLIENTE.sumar_puntos(2)
        else:
            self.CLIENTE.sumar_puntos(3)
        
        if self.CLIENTE.get_puntos() >= 20:
            descuento = precio * 0.4

        self.SUCURSAL.aumentarPresupuesto(precio - descuento)
        print("Tierra del sabor: " + self.SUCURSAL.getUbicacion() + "\n" +
                "Cliente titular: " + self.CLIENTE.get_nombre() + "\n" +
                "Mesero encargado: " + self.mesero.getNombre() + "\n" +
                "Chef encargado: " + self.chef.getNombre() + "\n" +
                "Mesa #" + str(self.mesa.getId()) + "\n" + 
                "Productos: \n" +
                platos + 
                "Valor de la compra: $" + str(precio) + "\n" +
                "Descuento por ser cliente frecuente: $" + str(descuento) + "\n" + 
                "Precio total: $" + str(precio - descuento))
        print("Ingrese la calificación que desea darle al servicio(número entre 1 y 5)")
        calificacion = 0
        while calificacion < 1 or calificacion > 5:
            calificacion = entrada()
            if calificacion < 1 or calificacion > 5:
                print("Valor incorrecto, debe ser un número entre 1 y 5")
        self.CLIENTE.dar_calificacion(self.mesero, self.chef, calificacion)