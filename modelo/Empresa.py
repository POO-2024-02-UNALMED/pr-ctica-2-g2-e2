from Sucursal import Sucursal

class Empresa:
    deudas = 12000000
    renta = 5000000
    gastoRecursos = 15000000
    gastoSalarios = 90000000
    presupuestoTotal = 8000000
    presupuestoBruto = 40000000

    @staticmethod
    def solvencia():
        pasivos = Empresa.deudas + Empresa.gastoRecursos + Empresa.renta
        activos = Empresa.presupuestoBruto
        return activos/pasivos

    @staticmethod
    def verFinanzas():
        return ("Deudas crediticias: $" + str(round(Empresa.deudas/1000000)) + "M\n" + 
                "Renta: $" + str(round(Empresa.deudas/1000000)) + "M\n" + 
                "Gasto en salarios: $" + str(round(Empresa.gastoSalarios/1000000)) + "M\n" + 
                "Gasto en recursos: $" + str(round(Empresa.gastoRecursos/1000000)) + "M\n" +
                "Capital bruto: $" + str(round(Empresa.presupuestoBruto/1000000)) + "M\n" + 
                "Capital neto: $" + str(round(Empresa.presupuestoTotal/1000000)) + "M\n" + 
                "Solvencia: " + str(round(Empresa.solvencia(),2)))
    
    @staticmethod
    def calcularFinanzas():
        pass
    
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