class Maestro:
    def __init__(self, nombre, disponibilidad, tipo):
        self.nombre = nombre
        self.disponibilidad = disponibilidad  # Disponibilidad es un diccionario 
        # Ejemplo: { "lunes": [[7, 10], ...]}
        self.tipo = tipo

    # Método para verificar si el maestro está disponible en un día y un número de bloques de horas
    def esta_disponible(self, dia, bloques_requeridos):
        if dia in self.disponibilidad:
            bloques_disponibles = 0
            for bloque in self.disponibilidad[dia]:
                bloques_disponibles += 1  # Cada bloque cuenta como una hora disponible
                if bloques_disponibles >= bloques_requeridos:
                    return True
        return False

    # Método para asignar bloques de horas a un maestro y ajustar su disponibilidad
    def asignar_horas(self, dia, bloques_requeridos):
        if dia in self.disponibilidad:
            bloques_disponibles = 0
            for i, bloque in enumerate(self.disponibilidad[dia]):
                bloques_disponibles += 1
                if bloques_disponibles == bloques_requeridos:
                    # Remover los bloques ya asignados
                    del self.disponibilidad[dia][:i+1]
                    return True
        return False

def organizar_profesores(profesores):
    contratados = [profesor for profesor in profesores if profesor.tipo == 'contrato']
    estrictos = [profesor for profesor in profesores if profesor.tipo == 'estricto']
    tiempo_completo = [profesor for profesor in profesores if profesor.tipo == 'tiempo completo']
    
    return contratados + estrictos + tiempo_completo