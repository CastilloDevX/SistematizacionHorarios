class Horario:
    def __init__(self, bloques_horarios):
        self.bloques_horarios = bloques_horarios  # Lista de bloques de horas [[7,8], [8,9], ...]
        self.horario_carreras = {}  # Diccionario para almacenar el horario de cada carrera por semestre

    # Método para asignar una materia a un profesor en un día y semestre específico
    def asignar_materia(self, carrera, semestre, materia, bloques_requeridos, profesor, dia):
        if profesor.asignar_horas(dia, bloques_requeridos):
            if carrera not in self.horario_carreras:
                self.horario_carreras[carrera] = {}
            if semestre not in self.horario_carreras[carrera]:
                self.horario_carreras[carrera][semestre] = {}
            if dia not in self.horario_carreras[carrera][semestre]:
                self.horario_carreras[carrera][semestre][dia] = []

            # Asignamos los bloques horarios a la materia y profesor
            for i in range(bloques_requeridos):
                self.horario_carreras[carrera][semestre][dia].append({
                    'materia': materia,
                    'profesor': profesor.nombre,
                    'bloque': self.bloques_horarios[i]
                })

    # Método para generar el horario secuencialmente para cada semestre
    def generar_horario_secuencial(self):
        horario_secuencial = {}
        
        for carrera, semestres in self.horario_carreras.items():
            horario_secuencial[carrera] = {}
            for semestre, dias in semestres.items():
                horario_secuencial[carrera][semestre] = {}
                for dia, clases in dias.items():
                    horario_secuencial[carrera][semestre][dia] = clases  # Guardamos las clases asignadas para cada día
        return horario_secuencial

def asignar_horarios(profesores, asignaturas, horario):
    dias = ['lunes', 'martes', 'miércoles', 'jueves', 'viernes']
    for carrera, semestres in asignaturas.items():
        for semestre, materias in semestres.items():
            for materia, bloques_requeridos in materias.items():
                for dia in dias:
                    for profesor in profesores:
                        if profesor.esta_disponible(dia, bloques_requeridos):
                            horario.asignar_materia(carrera, semestre, materia, bloques_requeridos, profesor, dia)
                            break  # Pasar a la siguiente materia después de asignarla