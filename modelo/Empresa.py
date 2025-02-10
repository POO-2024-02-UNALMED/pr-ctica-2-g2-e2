from Empleado import Empleado

class Empresa:
    deudas = 12000000
    renta = 0
    gastoRecursos = 0
    gastoSalarios = 0
    presupuestoTotal = 0
    presupuestoBruto = 0

    @staticmethod
    def solvencia():
        pasivos = Empresa.deudas + Empresa.gastoRecursos + Empresa.renta
        activos = Empresa.presupuestoBruto
        return activos/pasivos

    @staticmethod
    def verFinanzas():
        return ("Deudas crediticias: $" + str(round(Empresa.deudas/1000000)) + "M\n" + 
                "Renta: $" + str(round(Empresa.renta/1000000)) + "M\n" + 
                "Gasto en salarios: $" + str(round(Empresa.gastoSalarios/1000000)) + "M\n" + 
                "Gasto en recursos: $" + str(round(Empresa.gastoRecursos/1000000)) + "M\n" +
                "Capital bruto: $" + str(round(Empresa.presupuestoBruto/1000000)) + "M\n" + 
                "Capital neto: $" + str(round(Empresa.presupuestoTotal/1000000)) + "M\n" + 
                "Solvencia: " + str(round(Empresa.solvencia(),2)))
    
    @staticmethod
    def calcularFinanzas(sucursales):
        personal = Empleado.getPersonal()
        Empresa.renta = 1000000 * len(sucursales)
        Empresa.gastoSalarios = 0
        Empresa.gastoRecursos = 0
        Empresa.presupuestoBruto = 0
        for empleado in personal:
            Empresa.gastoSalarios += (empleado.getSueldo() * 12)
        for sucursal in sucursales:
            Empresa.gastoRecursos += sucursal.getGasto()
            Empresa.presupuestoBruto += sucursal.getPresupuesto()
        Empresa.presupuestoTotal = Empresa.presupuestoBruto - Empresa.renta - Empresa.gastoRecursos
    
    @staticmethod
    def pagarDeudas(sucursales):
        paga = 0
        for sucursal in sucursales:
            if sucursal.getPresupuesto() - 20000000 < 40000000: continue
            paga += 20000000
            sucursal.restarPresupuesto(20000000)
        Empresa.deudas -= paga
        return paga
    
    @staticmethod
    def endeudar(suma):
        Empresa.deudas += suma

    @staticmethod
    def getDeudas(): return Empresa.deudas

    @staticmethod
    def getRenta(): return Empresa.renta

    @staticmethod
    def getGastoRecursos(): return Empresa.gastoRecursos

    @staticmethod
    def getGastoSalarios(): return Empresa.gastoSalarios

    @staticmethod
    def getPresupuesto(): return Empresa.presupuestoTotal

    @staticmethod
    def getBruto(): return Empresa.presupuestoBruto

    @staticmethod
    def setDeudas(deudas): Empresa.deudas = deudas

    @staticmethod
    def setRenta(renta): Empresa.renta = renta

    @staticmethod
    def setGastoRecursos(gasto): Empresa.gastoRecursos = gasto

    @staticmethod
    def setGastoSalarios(gasto): Empresa.gastoSalarios = gasto

    @staticmethod
    def setPresupuesto(presupuesto): Empresa.presupuestoTotal = presupuesto

    @staticmethod
    def setBruto(presupuesto): Empresa.presupuestoBruto = presupuesto