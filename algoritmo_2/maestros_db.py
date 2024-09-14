from classes.maestro import Maestro

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