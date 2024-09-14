from db import maestros, asignaturas
from classes.horario import Horario, asignar_horarios
from classes.maestro import Maestro, organizar_profesores

# Crear el horario con los bloques de horas definidos
horario = Horario([[7, 8], [8, 9], [9, 10], [10, 11], [11, 12], [12, 13]])

# Organizar los profesores por disponibilidad
profesores_ordenados = organizar_profesores(maestros)

# Asignar las materias a los profesores
asignar_horarios(profesores_ordenados, asignaturas, horario)

# Generar el horario secuencial sin horas libres
horario_secuencial_final = horario.generar_horario_secuencial()

# Imprimir el horario final para cada carrera, semestre y día
for carrera, semestres in horario_secuencial_final.items():
    print(f"Horario para {carrera}:")
    for semestre, dias in semestres.items():
        print(f"  Semestre {semestre}:")
        for dia, clases in dias.items():
            print(f"    Día: {dia}")
            for clase in clases:
                print(f"      {clase['bloque'][0]}-{clase['bloque'][1]}: {clase['materia']} con {clase['profesor']}")
