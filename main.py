from db.carreras import carreras_materias
from db.maestros import maestros_fdi

class Maestro:
    def __init__(self, nombre, tipo, tiempo_trabajo, materias):
        self.nombre = nombre
        self.tipo = tipo
        self.tiempo_trabajo = tiempo_trabajo  # Disponibilidad: {"lunes": [[7, 11], [13, 16]], ...}
        self.materias = materias  # Materias: {"isc": ["logica de programación", "calculo diferencial", ...]}
        self.horas_asignadas = 0

class Horario:
    def __init__(self, grupos_por_carrera):
        # Inicializa una estructura de horarios de 7AM a 9PM por día, carrera y grupo
        self.horario_por_grupo = {
            carrera: {
                f"grupo_{g}": {dia: [[] for _ in range(7, 22)] for dia in ["lunes", "martes", "miercoles", "jueves", "viernes"]}
                for g in range(1, num_grupos+1)
            } for carrera, num_grupos in grupos_por_carrera.items()
        }

    def agregar_clase(self, carrera, grupo, dia, hora_inicio, hora_fin, maestro, materia):
        # Verificamos si la materia ya fue asignada al grupo en esa carrera
        for dia_horas in self.horario_por_grupo[carrera][grupo].values():
            if any(materia in clase for clase in dia_horas if clase):
                return False  # La materia ya ha sido asignada a este grupo

        # Asignamos la clase al grupo y al horario especificado
        for hora in range(hora_inicio, hora_fin):
            if self.horario_por_grupo[carrera][grupo][dia][hora-7]:  # Verificamos si la hora ya está ocupada
                return False
        for hora in range(hora_inicio, hora_fin):
            self.horario_por_grupo[carrera][grupo][dia][hora-7] = (maestro.nombre, materia)
        maestro.horas_asignadas += (hora_fin - hora_inicio)
        return True

    def imprimir_horario_por_carrera(self):
        for carrera, grupos in self.horario_por_grupo.items():
            print(f"\n--- Horarios para la carrera de {carrera.upper()} ---")
            for grupo, horario in grupos.items():
                print(f"\n{grupo.upper()}:")
                for dia, horas in horario.items():
                    print(f"\n{dia.capitalize()}:")
                    for hora in range(7, 22):
                        if horas[hora-7]:  # Si hay algo asignado en esa hora
                            maestro, materia = horas[hora-7]
                            print(f"- {hora}:00 a {hora+1}:00 -> {materia} por {maestro}")
                        #else:
                            #print(f"- {hora}:00 a {hora+1}:00 -> Libre")

def asignar_horarios(maestros, carreras, grupos_por_carrera):
    # Ordenar por prioridad: vinculación -> base -> tiempo completo
    maestros_vinculacion = [m for m in maestros if m.tipo == "vinculacion"]
    maestros_base = [m for m in maestros if m.tipo == "base"]
    maestros_tiempo_completo = [m for m in maestros if m.tipo == "tiempo completo"]

    horario_final = Horario(grupos_por_carrera)

    # Asignar primero maestros de vinculación
    for maestro in maestros_vinculacion:
        asignar_materias(maestro, horario_final, carreras, grupos_por_carrera)

    # Luego asignar maestros de base
    for maestro in maestros_base:
        asignar_materias(maestro, horario_final, carreras, grupos_por_carrera)

    # Finalmente, asignar maestros de tiempo completo
    for maestro in maestros_tiempo_completo:
        asignar_materias(maestro, horario_final, carreras, grupos_por_carrera)

    return horario_final

def asignar_materias(maestro, horario, carreras, grupos_por_carrera):
    for carrera, materias in maestro.materias.items():
        if carrera == "isc" or carrera == "its" or carrera == "ica":
            for materia in materias:
                for grupo in range(1, grupos_por_carrera[carrera] + 1):  # Asignar a cada grupo en la carrera
                    for dia, bloques in maestro.tiempo_trabajo.items():
                        bloques.sort()  # Aseguramos que los bloques se asignen en orden de menor a mayor
                        for bloque in bloques:
                            if maestro.horas_asignadas >= 24:  # Máximo de 24 horas a la semana
                                return
                            hora_inicio, hora_fin = bloque
                            # Intentamos llenar el bloque completo de manera secuencial
                            if horario.agregar_clase(carrera, f"grupo_{grupo}", dia, hora_inicio, hora_fin, maestro, materia):
                                print(f"Clase asignada: {maestro.nombre} enseña {materia} en {carrera} (grupo {grupo}) el {dia} de {hora_inicio} a {hora_fin}")
                                break

# Define el número de grupos por carrera (puede variar)
grupos_por_carrera = {
    "isc": 2,  # 3 grupos en ISC
    "its": 1,  # 2 grupos en IME
    "ica": 4,   # 1 grupo en IE
    # Agrega más carreras y su número de grupos aquí
}

# Asignar horarios
horario_final = asignar_horarios(maestros_fdi, carreras_materias, grupos_por_carrera)

# Imprimir el horario final por carrera y por grupo
horario_final.imprimir_horario_por_carrera()
