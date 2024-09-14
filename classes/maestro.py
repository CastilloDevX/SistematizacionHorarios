class Maestro:
    def __init__(self, nombre, tipo, tiempo_trabajo, materias):
        self.nombre = nombre
        
        self.tipo = tipo  # "vinculacion", "base", "tiempo completo"
        
        self.tiempo_trabajo = tiempo_trabajo  # {"lunes": [[7, 11], [13, 16]], ...}
        
        self.materias = materias  # {"isc": ["logica", "calculo"], "its": ["calculo", "fisica"]}
        
        self.horas_asignadas = 0  # Mantener un registro de horas asignadas