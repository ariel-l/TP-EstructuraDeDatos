def buscar_historial (historial, descripcion):
    if len(historial) == 0:
        return False
    if historial[0] == descripcion:
        return True
    return buscar_historial(historial[1:], descripcion)

# Historial del paciente
historial = [
    "Consulta inicial por dolor de cabeza",
    "Diagnóstico de migraña",
    "Tratamiento con analgésicos"
]

# Buscar eventos en el historial
print(buscar_historial(historial, "Diagnóstico de migraña"))  # True
print(buscar_historial(historial, "Radiografía de tórax"))    # False
