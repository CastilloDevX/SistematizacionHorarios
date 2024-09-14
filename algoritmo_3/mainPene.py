class Maestro:
    def __init__(self, nombre, tipo, tiempo_trabajo, materias):
        self.nombre = nombre
        self.tipo = tipo
        self.tiempo_trabajo = tiempo_trabajo
        self.materias = materias
        self.horas_asignadas = 0
        self.horario = {}  # Para almacenar el horario final asignado al maestro

# Para almacenar los horarios de cada carrera
horarios_carreras = {
    "isc": {},
    "its": {},
    "ime": {},
    "ie": {},
    "im": {},
    "ica": {}
}

def asignar_horarios(maestros, demanda_materias):
    # Paso 1: Clasificar maestros por tipo
    maestros_vinculacion = [m for m in maestros if m.tipo == "vinculacion"]
    maestros_base = [m for m in maestros if m.tipo == "base"]
    maestros_tiempo_completo = [m for m in maestros if m.tipo == "tiempo-completo"]
    
    # Paso 2: Asignar horarios a los maestros de vinculación primero
    for maestro in maestros_vinculacion:
        asignar_horario_maestro(maestro, demanda_materias)

    # Paso 3: Asignar horarios a los maestros base
    for maestro in maestros_base:
        asignar_horario_maestro(maestro, demanda_materias, min_horas=12, max_horas=24)

    # Paso 4: Asignar horarios a los maestros de tiempo completo
    for maestro in maestros_tiempo_completo:
        asignar_horario_maestro(maestro, demanda_materias, max_horas=24)

def asignar_horario_maestro(maestro, demanda_materias, min_horas=0, max_horas=None):
    # Recorrer cada día disponible del maestro
    for dia, horas in maestro.tiempo_trabajo.items():
        if dia not in maestro.horario:
            maestro.horario[dia] = []  # Inicializa el horario del día si no está
        
        for bloque in horas:
            inicio, fin = bloque
            duracion = fin - inicio
            
            # Revisar si el maestro tiene materias que impartir para las carreras
            for carrera, materias in maestro.materias.items():
                for materia in materias:
                    if demanda_materias.get(carrera, {}).get(materia, 0) > 0:
                        # Asignar las clases dentro del bloque de tiempo del maestro
                        horas_asignadas = min(duracion, demanda_materias[carrera][materia])
                        maestro.horas_asignadas += horas_asignadas
                        demanda_materias[carrera][materia] -= horas_asignadas
                        
                        # Guardar el horario asignado al maestro
                        maestro.horario[dia].append((inicio, inicio + horas_asignadas, materia, carrera))
                        
                        # Guardar el horario asignado a la carrera
                        if carrera not in horarios_carreras:
                            horarios_carreras[carrera] = {}
                        if materia not in horarios_carreras[carrera]:
                            horarios_carreras[carrera][materia] = []
                        horarios_carreras[carrera][materia].append((dia, inicio, inicio + horas_asignadas, maestro.nombre))
                        
                        # Reducir la duración de horas asignadas en este bloque
                        duracion -= horas_asignadas
                        inicio += horas_asignadas  # Avanzamos el inicio al final de la clase asignada

                        if max_horas and maestro.horas_asignadas >= max_horas:
                            return  # El maestro ya ha cumplido su máximo de horas

                        # Si ya no tiene más horas en este bloque, continuar
                        if duracion <= 0:
                            break
        
        # Si el maestro no ha completado su mínimo de horas
        if min_horas and maestro.horas_asignadas < min_horas:
            print(f"Advertencia: El maestro {maestro.nombre} no ha completado sus horas mínimas.")

# Imprimir el horario de todos los maestros
def imprimir_horarios_maestros(maestros):
    print("\n--- Horarios de Maestros ---")
    for maestro in maestros:
        print(f"Maestro: {maestro.nombre} ({maestro.tipo})")
        for dia, clases in maestro.horario.items():
            for clase in clases:
                inicio, fin, materia, carrera = clase
                print(f"  {dia}: {inicio} - {fin} hrs | {materia} ({carrera})")
        print()

# Imprimir el horario de cada carrera y sus materias
def imprimir_horarios_carreras():
    print("\n--- Horarios de Carreras ---")
    for carrera, materias in horarios_carreras.items():
        print(f"Carrera: {carrera.upper()}")
        for materia, clases in materias.items():
            print(f"  Materia: {materia}")
            for clase in clases:
                dia, inicio, fin, maestro = clase
                print(f"    {dia}: {inicio} - {fin} hrs | Impartido por {maestro}")
        print()

# Simulación de demanda de materias para cada carrera
demanda_materias = {
    "isc": {"programacion": 10, "calculo": 8, "fisica": 6},
    "its": {"fisica": 8, "calculo": 10, "quimica": 6},
    "ime": {"fisica": 6, "ingles": 12},
    "ie": {"calculo": 10, "fisica": 6},
    "im": {"logica": 10, "fisica": 8},
    "ica": {"ingles": 8}
}

# Lista de maestros
maestros_fdi = [
    Maestro("Juan", "vinculacion", 
            {"lunes": [[8, 10], [13, 15]], "miercoles": [[10, 12]]}, 
            {"isc": ["ingles"], "its": ["ingles"]}),
    
    Maestro("Ana", "base", 
            {"martes": [[7, 10], [12, 14]], "jueves": [[9, 12]]}, 
            {"ime": ["calculo"], "ie": ["fisica"]}),

    Maestro("Carlos", "tiempo-completo", 
            {"lunes": [[8, 12]], "miercoles": [[8, 12]]}, 
            {"isc": ["programacion"], "im": ["algoritmos"]}),
            
    Maestro("Laura", "vinculacion", 
            {"miercoles": [[10, 12], [13, 15]], "viernes": [[8, 10]]}, 
            {"ime": ["ingles"], "ie": ["ingles"]}),
        
    Maestro("Pedro", "base", 
            {"lunes": [[7, 11], [13, 16]], "martes": [[9, 11], [14, 16]]}, 
            {"isc": ["matematicas"], "its": ["fisica"]}),
        
    Maestro("Lucía", "vinculacion", {"jueves": [[9, 11], [14, 16]]}, 
            {"ie": ["ingles"], "im": ["ingles"]}),
        
    Maestro("Roberto", "tiempo-completo", 
            {"martes": [[7, 11], [13, 17]], "jueves": [[8, 12], [14, 18]]},
            {"ime": ["termodinamica"], "ie": ["dibujo tecnico"]}),
        
    Maestro("Elena", "base", 
            {"miércoles": [[8, 12], [13, 15]], "viernes": [[9, 12]]}, 
            {"isc": ["circuitos electricos"], "ime": ["fisica"]}),
        
    Maestro("Alberto", "vinculacion", 
            {"martes": [[7, 9], [14, 16]], "jueves": [[11, 13]]}, 
            {"im": ["ingles"], "isc": ["ingles"]}),
    Maestro("Andrea", "tiempo-completo", 
            {"lunes": [[9, 13], [14, 17]], "jueves": [[8, 12], [13, 15]]}, 
            {"im": ["logica"], "its": ["programacion"]}),

    Maestro("Fernando", "vinculacion", 
            {"martes": [[9, 11]], "viernes": [[10, 12]]}, 
            {"ime": ["ingles"], "ie": ["ingles"]}),
    
    Maestro("María", "base", 
            {"lunes": [[7, 10], [14, 17]], "miercoles": [[8, 11]]}, 
            {"its": ["quimica"], "im": ["fisica"]}),

    Maestro("Miguel", "tiempo-completo", 
            {"martes": [[8, 12], [14, 16]], "jueves": [[9, 13], [14, 16]]}, 
            {"isc": ["estructuras"], "ie": ["calculo"]}),

    Maestro("Sofía", "vinculacion", 
            {"jueves": [[9, 11], [14, 16]]},
            {"ime": ["ingles"], "ica": ["ingles"]}),
        
    Maestro("Luis", "base", 
            {"miercoles": [[9, 12], [14, 16]], "viernes": [[8, 11]]}, 
            {"isc": ["matematicas"], "its": ["calculo"]}),
    
    Maestro("Javier", "tiempo-completo", 
            {"lunes": [[8, 12], [13, 16]], "miercoles": [[7, 10], [12, 14]]}, 
            {"im": ["fisica"], "ime": ["quimica"]}),

    Maestro("Daniela", "vinculacion", 
            {"martes": [[9, 11]], "viernes": [[10, 12]]}, 
            {"ie": ["ingles"], "isc": ["ingles"]}),

    Maestro("Raúl", "base", 
            {"lunes": [[7, 10], [14, 16]], "jueves": [[8, 11]]}, 
            {"its": ["fisica"], "ime": ["quimica"]}),
    
    Maestro("Carla", "tiempo-completo", 
            {"miercoles": [[8, 12], [13, 16]], "viernes": [[9, 13]]}, 
            {"isc": ["algoritmos"], "im": ["logica"]}),
    
    Maestro("Oscar", "vinculacion", 
            {"lunes": [[8, 10], [13, 15]], "miercoles": [[10, 12]]}, 
            {"ica": ["ingles"], "im": ["ingles"]}),
    
    Maestro("Natalia", "base", 
            {"martes": [[7, 10], [14, 16]], "jueves": [[9, 12]]}, 
            {"ie": ["quimica"], "its": ["fisica"]}),
    
    Maestro("Patricia", "tiempo-completo", 
            {"lunes": [[8, 12], [14, 16]], "viernes": [[9, 13], [14, 16]]}, 
            {"ime": ["fisica"], "im": ["quimica"]}),
    
    Maestro("Iván", "vinculacion", 
            {"lunes": [[10, 12], [14, 16]]}, 
            {"ie": ["ingles"], "isc": ["ingles"]}),
    
    Maestro("Adriana", "base", 
            {"martes": [[8, 12], [14, 16]], "jueves": [[7, 10]]}, 
            {"isc": ["calculo"], "its": ["matematicas"]}),
    
    Maestro("César", "tiempo-completo", 
            {"lunes": [[8, 12], [14, 17]], "viernes": [[9, 13], [14, 16]]}, 
            {"ime": ["quimica"], "ie": ["fisica"]}),
   
    Maestro("Teresa", "vinculacion", 
            {"jueves": [[9, 11], [14, 16]]}, 
            {"ime": ["ingles"], "ica": ["ingles"]}),
   
    Maestro("Eduardo", "base",
            {"miércoles": [[9, 12], [13, 15]], "viernes": [[8, 11]]}, 
            {"isc": ["estructuras"], "its": ["calculo"]}),
    
    Maestro("Rosa", "tiempo-completo", 
            {"lunes": [[9, 13], [14, 16]], "jueves": [[9, 12], [14, 17]]}, 
            {"im": ["fisica"], "ime": ["quimica"]}),
    
    Maestro("Julio", "vinculacion", 
            {"martes": [[8, 10]], "viernes": [[10, 12]]}, 
            {"ie": ["ingles"], "isc": ["ingles"]}),
    
    Maestro("Verónica", "base", 
            {"lunes": [[7, 10], [14, 17]], "miércoles": [[9, 11]]}, 
            {"its": ["fisica"], "im": ["quimica"]}),
    
    Maestro("David", "tiempo-completo", 
            {"martes": [[8, 12], [14, 17]], "jueves": [[9, 13], [14, 16]]}, 
            {"isc": ["programacion"], "ie": ["calculo"]}),
    
    Maestro("Cristina", "vinculacion",
            {"jueves": [[9, 11], [14, 16]]}, 
            {"ime": ["ingles"], "ica": ["ingles"]}),
    
    Maestro("José", "base", 
            {"miércoles": [[9, 12], [14, 16]], "viernes": [[8, 11]]}, 
            {"isc": ["matematicas"], "its": ["fisica"]}),
    
    Maestro("Manuel", "tiempo-completo", 
            {"lunes": [[8, 12], [13, 16]], "miércoles": [[7, 10], [12, 14]]}, 
            {"im": ["fisica"], "ime": ["quimica"]}),
    
    Maestro("Gloria", "vinculacion", 
            {"martes": [[9, 11]], "viernes": [[10, 12]]}, 
            {"ie": ["ingles"], "isc": ["ingles"]}),
    
    Maestro("Isabel", "base", 
            {"lunes": [[7, 10], [14, 16]], "jueves": [[8, 11]]}, 
            {"its": ["fisica"], "ime": ["quimica"]}),
    
    Maestro("Pablo", "tiempo-completo", 
            {"miércoles": [[8, 12], [13, 16]], "viernes": [[9, 13]]}, 
            {"isc": ["algoritmos"], "im": ["logica"]}),
]
# Ejecutar la asignación de horarios
asignar_horarios(maestros_fdi, demanda_materias)

# Imprimir resultados
imprimir_horarios_maestros(maestros_fdi)
imprimir_horarios_carreras()