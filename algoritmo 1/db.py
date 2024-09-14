from classes.horario import Horario
from classes.maestro import Maestro

# Crear instancias de profesores con disponibilidad por días y bloques de horas
maestros = [
    Maestro("Profe A", {
            "lunes": [[7, 8], [8, 9], [10, 11]], 
            "viernes": [[10, 11], [12, 13]]
        }, "contrato"),
    Maestro("Profe B", {
            "lunes": [[7, 8], [9, 10]],
            "miércoles": [[8, 9], [9, 10]]
        }, "cele"),
    Maestro("Profe C", {
        "martes": [[8, 9], [9, 10]], 
        "jueves": [[10, 11], [11, 12]]
        }, "tiempo completo"),
    Maestro("Profe D", {
        "miercoles": [[8, 9], [9, 10]], 
        "jueves": [[10, 11], [11, 12]]
        }, "tiempo completo"),
    Maestro("Profe E", {
        "martes": [[10, 15]], 
        "jueves": [[10, 11], [11, 12]]
        }, "tiempo completo"),
    Maestro("Profe F", {
        "martes": [[8, 9], [9, 10]], 
        "jueves": [[10, 11], [11, 12]]
        }, "tiempo completo"),
    Maestro("Profe G", {
        "lunes": [[8, 15]], 
        "martes": [[8, 15]],
        "miercoles": [[8, 15]],
        "jueves": [[8, 15]],
        "viernes": [[8, 15]]
        }, "tiempo completo"),
    Maestro("Profe H", {
        "lunes": [[8, 15]], 
        "martes": [[8, 15]],
        "miercoles": [[8, 15]],
        "jueves": [[8, 15]],
        "viernes": [[8, 15]]
        }, "tiempo completo"),
    Maestro("Profe I", {
        "lunes": [[8, 15]], 
        "martes": [[8, 15]],
        "miercoles": [[8, 15]],
        "jueves": [[8, 15]],
        "viernes": [[8, 15]]
        }, "tiempo completo"),
    Maestro("Profe J", {
        "lunes": [[8, 15]], 
        "martes": [[8, 15]],
        "miercoles": [[8, 15]],
        "jueves": [[8, 15]],
        "viernes": [[8, 15]]
        }, "tiempo completo"),
    Maestro("Profe K", {
        "lunes": [[8, 15]], 
        "martes": [[8, 15]],
        "miercoles": [[8, 15]],
        "jueves": [[8, 15]],
        "viernes": [[8, 15]]
        }, "tiempo completo"),
    Maestro("Profe L", {
        "lunes": [[8, 15]], 
        "martes": [[8, 15]],
        "miercoles": [[8, 15]],
        "jueves": [[8, 15]],
        "viernes": [[8, 15]]
        }, "tiempo completo"),
    Maestro("Profe M", {
        "lunes": [[8, 15]], 
        "martes": [[8, 15]],
        "miercoles": [[8, 15]],
        "jueves": [[8, 15]],
        "viernes": [[8, 15]]
        }, "tiempo completo"),
    Maestro("Profe M", {
        "lunes": [[8, 15]], 
        "martes": [[8, 15]],
        "miercoles": [[8, 15]],
        "jueves": [[8, 15]],
        "viernes": [[8, 15]]
        }, "tiempo completo"),
    Maestro("Profe O", {
        "lunes": [[8, 15]], 
        "martes": [[8, 15]],
        "miercoles": [[8, 15]],
        "jueves": [[8, 15]],
        "viernes": [[8, 15]]
        }, "tiempo completo"),
    Maestro("Profe P", {
        "lunes": [[8, 15]], 
        "martes": [[8, 15]],
        "miercoles": [[8, 15]],
        "jueves": [[8, 15]],
        "viernes": [[8, 15]]
        }, "tiempo completo"),
]
# Definir asignaturas por carrera y semestre con número de bloques requeridos
asignaturas = {
    "ISC": {
        1: {"Logica de programacion": 2, "Expresion grafica": 2},
        2: {"Lenguaje de programacion I": 4, "Administracion General": 4},
        3: {"Lenguaje de programacion II": 3, "Matematicas para la computacion": 2}
    },
    "ITS": {
        1: {"Programación": 2, "Base de Datos": 2},
        2: {"POO": 4, "Matematicas para la computación": 4},
        3: {"Algoritmos": 3, "Redes": 2}
    },
    "IME": {
        1: {"Física": 4, "Termodinámica": 2},
        2: {"Programacion": 2, "Otra materia": 2},
        3: {"Mecánica": 3, "Cálculo": 2}
    },
    "IE": {
        1: {"Cálculo": 2, "Circuitos Eléctricos": 3},
        2: {"Electromagnetismo": 3, "Matemáticas": 2}
    },
    "IM": {
        1: {"Estática": 3, "Dinámica": 2},
        2: {"Mecánica de Materiales": 3, "Ingeniería de Control": 2}
    },
    "ICA": {
        1: {"Materiales de Construcción": 4, "Diseño Estructural": 2},
        2: {"Geotecnia": 3, "Hidráulica": 2}
    }
}