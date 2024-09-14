from classes.maestro import Maestro
from algoritmo_2.maestros_db import maestros_fdi # Base de datos simulada

def ordenar_maestros():
    maestros_vinculacion = sorted([m for m in maestros_fdi if m.tipo == "vinculacion"], key=lambda m: sum([fin - inicio for horarios in m.tiempo_trabajo.values() for inicio, fin in horarios]))
    maestros_base = sorted([m for m in maestros_fdi if m.tipo == "base"], key=lambda m: sum([fin - inicio for horarios in m.tiempo_trabajo.values() for inicio, fin in horarios]))
    maestros_tiempo_completo = sorted([m for m in maestros_fdi if m.tipo == "tiempo completo"], key=lambda m: sum([fin - inicio for horarios in m.tiempo_trabajo.values() for inicio, fin in horarios]))
    
    return maestros_vinculacion + maestros_base + maestros_tiempo_completo

# Verificar si el maestro tiene una hora disponible para un día y rango de horas específico
def verificar_disponibilidad(maestro, dia, inicio, fin):
    if dia in maestro.tiempo_trabajo:
        for rango in maestro.tiempo_trabajo[dia]:
            if inicio >= rango[0] and fin <= rango[1]:  # Verificamos si la hora de inicio y fin están dentro de los horarios permitidos
                return True
    return False

horarios = {
    "isc": {
        "a":{},
        "b":{}
    },
    "its": {
        "a":{}
    },
    "ica": {
        "a":{},
        "b":{},
        "c":{}
    },
    "im":{
        "a":{},
        "b":{},
        "c":{}
    },

    "ime":{
        "a":{}
    },

    "ie": {
        "a":{}
    }
}

def asignar_horarios_carrera(maestros_ordenados, carrera):
    dias = ["lunes", "martes", "miércoles", "jueves", "viernes"]
    
    # Inicializamos el horario de la carrera
    horario = {"a": {}, "b": {}}  # Ejemplo: dos grupos 'a' y 'b'
    
    # Clasificamos los maestros en vinculacion, base y tiempo completo
    maestros_vinculacion = [m for m in maestros_ordenados if m.tipo == "vinculacion"]
    maestros_base = [m for m in maestros_ordenados if m.tipo == "base"]
    maestros_tiempo_completo = [m for m in maestros_ordenados if m.tipo == "tiempo completo"]

    # Control de asignaciones por día para cada maestro
    clases_por_dia = {dia: {} for dia in dias}

    # Control de horas ocupadas por grupo y día
    horas_ocupadas = {grupo: {dia: set() for dia in dias} for grupo in horario.keys()}

    # Registro de materias asignadas por grupo para evitar duplicaciones
    materias_asignadas = {grupo: set() for grupo in horario.keys()}

    # Función auxiliar para asignar horarios
    def asignar_horarios(maestros, grupo):
        for maestro in maestros:
            for dia in dias:
                if dia in clases_por_dia and maestro.nombre in clases_por_dia[dia]:
                    # El maestro ya tiene una clase en este día
                    continue
                
                # Inicia a las 7 am
                hora_actual = 7
                while hora_actual < 17:
                    # Verificamos si el maestro tiene disponibilidad ese día
                    if dia in maestro.tiempo_trabajo:
                        disponibilidad = maestro.tiempo_trabajo[dia]
                        for bloque in disponibilidad:
                            inicio, fin = bloque
                            if inicio <= hora_actual < fin and (hora_actual + 2) <= fin:
                                # Verificamos si el bloque está disponible en el horario del grupo
                                if hora_actual not in horas_ocupadas[grupo][dia] and (hora_actual + 2) not in horas_ocupadas[grupo][dia]:
                                    materias_maestro = maestro.materias.get(carrera, [])
                                    if materias_maestro:
                                        materia = materias_maestro[0]  # Tomamos la primera materia disponible
                                        
                                        # Verificamos que la materia no haya sido asignada ya en este grupo
                                        if materia not in materias_asignadas[grupo]:
                                            # Asignar de 2 a 4 horas para esta materia
                                            duracion_clase = min(4, fin - hora_actual)  # Aseguramos de no exceder el bloque disponible
                                            duracion_clase = max(2, duracion_clase)  # Mínimo de 2 horas
                                            
                                            # Asignamos la materia y bloque
                                            if dia not in horario[grupo]:
                                                horario[grupo][dia] = []
                                            horario[grupo][dia].append(((hora_actual, hora_actual + duracion_clase), maestro.nombre, materia))
                                            
                                            # Registrar la asignación del maestro y la materia
                                            clases_por_dia[dia][maestro.nombre] = materia
                                            horas_ocupadas[grupo][dia].update(range(hora_actual, hora_actual + duracion_clase))
                                            
                                            # Registrar la materia asignada al grupo para evitar duplicaciones
                                            materias_asignadas[grupo].add(materia)
                                            
                                            # Eliminar la materia del maestro para que no la repita
                                            maestro.materias[carrera].remove(materia)
                                            break
                    hora_actual += 2

    # Paso 1: Asignar horarios para los maestros de vinculación
    for grupo in horario.keys():
        asignar_horarios(maestros_vinculacion, grupo)
    
    # Paso 2: Asignar horarios para los maestros de base
    for grupo in horario.keys():
        asignar_horarios(maestros_base, grupo)
    
    # Paso 3: Asignar horarios para los maestros de tiempo completo
    for grupo in horario.keys():
        asignar_horarios(maestros_tiempo_completo, grupo)
    
    return horario
    
def imprimir_horario(horario, carrera):
    print(f"\n{carrera.upper()}")
    for grupo, dias in horario.items():
        print(f"\nGrupo {grupo.upper()}")
        for dia, clases in dias.items():
            print(f"{dia.capitalize()}:")
            for clase in clases:
                (inicio, fin), maestro, materia = clase
                print(f"- {inicio} a {fin} ({materia}) por {maestro}")

def establecer_horarios():
    # Ordenar maestros según su disponibilidad
    maestros_ordenados = ordenar_maestros()

    # Asignar horarios para todas las carreras y grupos
    for carrera in horarios:
        horario_generado = asignar_horarios_carrera(maestros_ordenados, carrera)
        imprimir_horario(horario_generado, carrera)

# Ejecutar la asignación de horarios
establecer_horarios()
