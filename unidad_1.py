class Paciente:
    def __init__(self, nombre, edad, ID, email, numero, cobertura):
        self.nom = nombre
        self.edad = edad
        self.ID = ID
        self.email = email
        self.num = numero
        self.cob = cobertura
        self.historial = []  # Historial vacío

    def __repr__(self):
        return f"Paciente(ID={self.ID}, nombre={self.nom}, edad={self.edad}, email={self.email})"
    
    def añadir_historial(self, evento):
        self.historial.append(evento)
        print(f"Evento '{evento}' añadido correctamente.")
    
    def eliminar_historial(self, descripcion):
        if descripcion in self.historial:
            self.historial.remove(descripcion)
            print(f"Evento '{descripcion}' eliminado correctamente.")
        else:
            print(f"No se encontró el evento: {descripcion}")

    def modificar_info(self, codigo, nombre=None, edad=None, email=None, numero=None):
        if codigo == self.ID:
            if nombre: self.nom = nombre
            if edad: self.edad = edad
            if email: self.email = email
            if numero: self.num = numero
            print("Información actualizada correctamente.")
        else:
            print("Código incorrecto. No se puede modificar la información.")
    
    def mostrar_informacion(self):
        print(f"--- Información del Paciente ---")
        print(f"Nombre: {self.nom}")
        print(f"Edad: {self.edad}")
        print(f"ID: {self.ID}")
        print(f"Email: {self.email}")
        print(f"Número: {self.num}")
        print(f"Cobertura: {self.cob}")
        print(f"Historial: {self.historial}")