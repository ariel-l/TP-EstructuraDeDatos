import heapq
from unidad_1 import Paciente

class UrgenciaMedica:
    def __init__(self):
        self.heap = []
    
    def agregar_paciente(self, paciente, gravedad):
        heapq.heappush(self.heap, (-gravedad, paciente))
        print(f"Paciente agregado: {paciente.nom}, Gravedad: {gravedad}")
    
    def atender_paciente(self):
        if self.heap:
            gravedad, paciente = heapq.heappop(self.heap)
            print(f"Atendiendo al paciente: {paciente.nom}, Gravedad: {-gravedad}")
            return paciente
        else:
            print("No hay pacientes en espera.")
            return None
    
    def mostrar_pacientes(self):
        if self.heap:
            print("Pacientes en espera:")
            for gravedad, paciente in sorted(self.heap, reverse=True):
                print(f"{paciente.nom}, Gravedad: {-gravedad}")
        else:
            print("No hay pacientes en espera.")

#EJEMPLO DE USO:

urgencia = UrgenciaMedica()

paciente1 = Paciente("Juan Pérez", 30, 1, "juan.perez@gmail.com", "123456789", "OSDE")
paciente2 = Paciente("María Gómez", 25, 2, "maria.gomez@gmail.com", "987654321", "OSDE")
paciente3 = Paciente("Carlos Ruiz", 40, 3, "carlos.ruiz@gmail.com", "555555555", "IOMA")

# Agregar pacientes con diferentes niveles de gravedad
urgencia.agregar_paciente(paciente1, gravedad=3)  
urgencia.agregar_paciente(paciente2, gravedad=5) 
urgencia.agregar_paciente(paciente3, gravedad=2)

# Mostrar pacientes en espera
urgencia.mostrar_pacientes()

# Atender pacientes
urgencia.atender_paciente()
urgencia.atender_paciente()

# Mostrar los pacientes restantes
urgencia.mostrar_pacientes()

