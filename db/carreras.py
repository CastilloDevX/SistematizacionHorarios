carreras_materias = {
    "isc": {
        1: ["Álgebra superior", "Cálculo diferencial" "Inglés 1", "Expresión gráfica","Geometría analítica", "Introducción a la ingenieria", "Lógica de programación", "Elaboración y presentión de textos"], 
        2: ["Física", "Administración general", "Álgebra lineal", "Cálculo integral", "Herramientas de la computación", "Inglés 2", "Lenguaje de programación 1", "Organización computacional"],
        3: [ "Lenguaje de programación 2", "Matemáticas para la computación", "Inglés 3", "Química", "Análisis de circuitos de CD", "Cálculo vectorial", "Contabilidad", "Fundamentos de probabilidad y estadística"],
        4: ["Estadística Aplicada", "Estructura de datos 1", "Inglés 4", "Programación de interfaces gráficas del usuario", "Economía para ingenieros", "Ecuaciones diferenciales", "Electrónica", "Métodos numéricos"],
        5: ["Arquitectura computacional", "Base de datos I(Inglés)", "Base de datos I", "Estructura de datos II", "Graficación", "Inglés 5", "Investigación de operaciones I", "Telecomunicaciones", "Administración de archivos"],
        6: ["Inglés 6", "Fundamentos de redes", "Inteligencia artificial", "Investigación de operaciones II", "Simulación", "Sistemas I", "Sistemas operativos", "Taller de base de datos (inglés)", "Taller de base de datos"],
        7: ["Base de datos II (ingles)", "Base de datos II", "Programación de aplicaciones WEB", "Redes I", "Sistemas II", "Sistemas inteligentes I", "Compiladores", "Ingeniería de software", "Metodología de la investigación", "Taller de emprendedores"],
        8: ["Administración de tecnologías de la información", "Desarrollo de aplicaciones móviles", "Gestión de proyectos de software", "Gestión de proyectos", "Legislación ética y profesional", "Recursos y necesidades de México", "Redes II", "Sistemas distribuidos", "Sistemas inteligentes II", "Temas selectos de programación", "Temas selectos de sistemas inteligentes", "Administración de servidores" ]
    },

    "its": {
        1:["metodología de la investigación", "alegebra y geometría analítica", "química", "introducción a la ingeniería", "fundamentos de la programación", "elaboración y presentación de textos", "inglés 1"],
        2:["educación ambiental para la sustentabilidad", "álgebra lineal", "cálculo diferencial e integral", "matemáticas discretas", "programación orientada a objetos", "deontología y responsabilidad social", "inglés 2"],
        3:["sistemas operativos", "probabilidad y estadisica", "cálculo vectorial", "lógica digital", "estructura de datos", "fisica 1", "inglés 3"],
        4:["base de datos 1", "electrónica", "ecuaciones diferenciales", "arquitectura de computadoras", "análisis y diseño de algoritmos", "fisica 2", "inglés 4"],
        5:["base de datos 2", "diseño web", "concurrencia y paralelismo", "sistemas embebidos", "programación avanzada", "redes de computadoras", "inglés 5"],
        6:["big data", "programación web", "inteligencia artificial", "desarrollo de aplicaciones móviles", "ingeniería de software", "interconexión de redes", "inglés 6"],
        7:["poryecto de desarrollo de videojuegos", "seguridad informática", "sistemas inteligentes", "tópicos avanzados de desarrollo de aplicaciones móviles", "diseño y arquitectura de software", "optativa 1", "calidad y pruebas de software"],
        8:["optativa 2", "computo en la nube", "optativa 3", "taller de emprendedores", "optativa 4", "optativa 5", "optativa 6"]
    },

    "ica": {
        1:["Dibujo constructivo", "Algebra y geometría analítica", "Calculo diferencial y integral", "introducción a la ingeniería", "Administración para ingenieros", "Programación", "inglés 1"],
        2:["Estadistica y dinamica","Algebra lineal", "Calculo vectorial","Elaboración y presentación de textos","Topografía","Contabilidad y finanzas","Ingles 2"],
        3:["Estructuras estadisticas", "Fundamentos de probabilidad y estadistica", "Ecuaciones diferenciales", "Construcción 1", "Geotecma 1","Metodología de la investigación", "Ingles 3"],
        4:["Mecanica de materiales","Metodos numericos","Hidraulica 1","Instalaciones en  los edificios","Geotecnia 1","Recursos humanos","Ingles 4"],
        5:["Ingenieria de sistemas", "Hidraulica 1","Construcción 2","Carreteras","Aspectos legales de la ingenieria","Ingles 5"],
        6:["Estructuras II","Ingenieria de transito","Hidrología superficial y subterranea","Programación y control de obra","Diseño y construcción de pavimentos","Recursos y necesidades de mexíco","Ingles 6"],
        7:["Estructuras 3","Sistemas de abastecimientos y recolección de aguas","Herramientas de computo para la ingenieria civil","Organización y evaluación de proyectos","introduccion a la investigación cientifica","optativa costas y obras maritimas","Optativa diseño de estructuras de mamposteria"],
        8:["Taller de emprendedores","Administración de empresas constructoras","Proyecto integrador","Rehabilitación y mantenimiento de infraestructuras","Optativa ingenieria sanitaria","Optativa geotecnia en graficación","Optativa Hidraulica e Hidrologia urbana","Optativa diseño de estructura de mamposteria"],
    }
}

for carrera, semestres in carreras_materias.items():
    for semestre, materias in semestres.items():
        # Convierte cada materia a minúsculas
        carreras_materias[carrera][semestre] = [materia.lower() for materia in materias]