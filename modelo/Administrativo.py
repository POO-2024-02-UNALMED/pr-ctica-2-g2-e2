class Administrativo:
    admins = []

    def __init__(self, nombre, cedula, contrasena):
        self.nombre = nombre
        self.cedula = cedula
        self.contrasena = contrasena
        Administrativo.admins.append(self)
        
    
    @staticmethod
    def verificarAdmin(cedula):
        for admin in Administrativo.admins:
            if admin.cedula == cedula:
                return admin
        return False
    
    def verificarCodigo(self, contrasena):
        if self.contrasena == contrasena:
            return True
        return False