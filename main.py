from unidad_1 import Paciente
from unidad_5 import UrgenciaMedica

class MenuPaciente:
    def __init__(self):
        self.paciente = Paciente("Juan Pérez", 30, 1234, "juan.perez@gmail.com", "123456789", "OSDE")
        self.urgencia = UrgenciaMedica()

    def mostrar_menu(self):
        while True:
            print("\n--- Menú Principal ---")
            print("1. Gestión de Paciente")
            print("2. Manejo de Urgencias")
            print("3. Salir")
            opcion = input("Selecciona una opción: ")

            if opcion == "1":
                self.menu_paciente()
            elif opcion == "2":
                self.menu_urgencias()
            elif opcion == "3":
                print("Saliendo del programa. ¡Hasta luego!")
                break
            else:
                print("Opción no válida. Por favor, intenta de nuevo.")

    def menu_paciente(self):
        while True:
            print("\n--- Menú de Gestión de Paciente ---")
            print("1. Añadir evento al historial")
            print("2. Eliminar evento del historial")
            print("3. Mostrar historial")
            print("4. Modificar información del paciente")
            print("5. Mostrar información del paciente")
            print("6. Volver al menú principal")
            opcion = input("Selecciona una opción: ")

            if opcion == "1":
                self.añadir_evento()
            elif opcion == "2":
                self.eliminar_evento()
            elif opcion == "3":
                self.mostrar_historial()
            elif opcion == "4":
                self.modificar_informacion()
            elif opcion == "5":
                self.mostrar_informacion()
            elif opcion == "6":
                break
            else:
                print("Opción no válida. Por favor, intenta de nuevo.")

    def añadir_evento(self):
        evento = input("Describe el evento médico: ")
        self.paciente.añadir_historial(evento)

    def eliminar_evento(self):
        descripcion = input("Introduce la descripción del evento a eliminar: ")
        self.paciente.eliminar_historial(descripcion)

    def mostrar_historial(self):
        print("\nHistorial del paciente:")
        if self.paciente.historial:
            for i, evento in enumerate(self.paciente.historial, 1):
                print(f"{i}. {evento}")
        else:
            print("El historial está vacío.")

    def modificar_informacion(self):
        print("\n--- Modificar Información ---")
        nombre = input("Nuevo nombre (deja en blanco para mantener el actual): ")
        edad = input("Nueva edad (deja en blanco para mantener el actual): ")
        email = input("Nuevo correo electrónico (deja en blanco para mantener el actual): ")
        telefono = input("Nuevo número de teléfono (deja en blanco para mantener el actual): ")

        self.paciente.modificar_info(
            codigo=self.paciente.ID,
            nombre=nombre if nombre else None,
            edad=int(edad) if edad else None,
            email=email if email else None,
            numero=telefono if telefono else None
        )

    def mostrar_informacion(self):
        self.paciente.mostrar_informacion()

    def menu_urgencias(self):
        while True:
            print("\n--- Menú de Urgencias ---")
            print("1. Agregar paciente a urgencias")
            print("2. Atender paciente")
            print("3. Mostrar pacientes en espera")
            print("4. Volver al menú principal")
            opcion = input("Selecciona una opción: ")

            if opcion == "1":
                gravedad = int(input("Introduce la gravedad del paciente (1-10): "))
                self.urgencia.agregar_paciente(self.paciente, gravedad)
            elif opcion == "2":
                self.urgencia.atender_paciente()
            elif opcion == "3":
                self.urgencia.mostrar_pacientes()
            elif opcion == "4":
                break
            else:
                print("Opción no válida. Por favor, intenta de nuevo.")


if __name__ == "__main__":
    menu = MenuPaciente()
    menu.mostrar_menu()
