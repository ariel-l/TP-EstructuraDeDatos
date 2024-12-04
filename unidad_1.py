class Paciente ():
    def __init__(self, nombre, edad, ID, email, numero, cobertura):
        self.nom = nombre
        self.edad = edad
        self.ID = ID
        self.email = email
        self.num = numero
        self.cob = cobertura
        self.historial = []
    def __repr__(self):
        return f"Paciente(ID={self.ID}, nombre={self.nom})"
    
    def añadir_historial (self, paciente):
        self.historial.append(paciente)
        print (f"Evento añadido correctamente")
    
    def eliminar_historial (self, descripcion):
        for elemento in self.historial:
            if elemento == descripcion:
                self.historial.remove(elemento)
                return
        print(f"La descripcion ingresada no existe")
    
    def modificar_info (self, codigo, nombre, edad, email, numero):
        if codigo == self.ID:
            self.nom = nombre
            self.edad = edad
            self.mail = email
            self.num = numero

# Crear un paciente
paciente = Paciente("Juan Pérez", 30, 1234, "juan.perez@gmail.com", "123456789", "OSDE")

# Añadir eventos al historial
paciente.añadir_historial("Consulta inicial por dolor de cabeza")
paciente.añadir_historial("Diagnóstico de migraña")
paciente.añadir_historial("Tratamiento con analgésicos")

# Mostrar historial
print("\nHistorial actual:")
print(paciente.historial)

# Eliminar un evento del historial
paciente.eliminar_historial("Diagnóstico de migraña")

# Mostrar historial actualizado
print("\nHistorial actualizado:")
print(paciente.historial)

# Modificar información del paciente
paciente.modificar_info(1234, nombre="Juan Carlos Pérez", edad=45, email="juan.carlos@gmail.com", numero=12345678)

# Mostrar información actualizada
print("\nInformación actualizada del paciente:")
print(paciente)
 