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
