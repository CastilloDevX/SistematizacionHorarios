from classes.maestro import Maestro

maestros_fdi = [
    Maestro("cristoper joel flores escalante", "base", 
            {"lunes": [[7, 13]],"miercoles": [[13, 15]], "viernes": [[9, 15]]}, 
            {"its": ["algebra y geometria analitica","probabilidad y estadistica"]}),
    
    Maestro("julio antonio gutierrez gonzalez", "base", 
            {"lunes": [[9, 11],[13, 15]], "martes": [[9, 13]],"miercoles": [[11, 13]],"jueves": [[7, 9],[11, 13]],"viernes": [[12, 14]]}, 
            {"its": ["elaboracion y presentacion de textos"],"its": ["metodologia de la investigacion"], "isc": ["elaboracion y presentacion de textos"], "ica": ["planeacion y organizacion de proyectos"]}),

    Maestro("manuel hector cosgaya quej", "base", 
            {"martes": [[7, 9]], "viernes": [[7, 9]]}, 
            {"isc": ["programacion"]}),
            
    Maestro("isabel del socorro silva leon", "vinculacion", 
            {"martes": [[11, 13]], "jueves": [[9, 11]]}, 
            {"its": ["quimica"]}),
        
    Maestro("contrato01", "contrato", 
            {"miercoles": [[7, 9]], "jueves": [[13, 14]]}, 
            {"its": ["introduccion a la ingenieria"]}),
        
    Maestro("contrato02", "contrato", 
            {"lunes": [[11, 13]],"jueves": [[11, 13]]}, 
            {"its": ["ingles"]}),

#okey ya mas clar

#el base tiene > de 12 horas
#el contrato no tiene nombre del maestros
#y el de vinculacion solo da una sola materia 

#//////////////////////////////////////////////////////////////////////////////////////// ADIEL
        
    Maestro("joel critofer flores escalante", "tiempo-completo", 
            {"lunes": [[9, 11]], "martes": [[11, 13]], "viernes":[[13,15]]},
            {"its": ["probabilidad y estadistica"]}),
        
    Maestro("roberto carlos canto canul", "base", 
            {"miercoles": [[15, 17]], "viernes": [[11, 13]]}, 
            {"its": ["Logica digital"]}),
        
    Maestro("Diana Concepcion Mex Alvarez", "vinculacion", 
            {"martes": [[13, 15]], "jueves": [[9,11]]}, 
            {"its": ["ingles"], "isc": ["ingles"]}),

    Maestro("gabriel ivan canto santana", "tiempo-completo", 
            {"marte": [[17, 19]], "miercoles": [[16, 18]], "jueves":[[17, 19]]}, 
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

    Maestro(
        "Chavez Molina José Manuel",
        "base",
        {
                "lunes": [[13, 15], [15, 16]],
                "martes": [[7, 9], [13, 15]],
                "jueves": [[7, 13]],
                "viernes": [[7, 10]]
        },
        {
                "its": ["Inglés 5"],
                "ica": ["Inglés 3"],
                "im": ["Inglés 3"],
                "ie": ["Inglés 4"],
                "ie": ["Inglés 6"]
        }),
    
    Maestro("contrato01", "tiempo-completo", 
            {"lunes": [[13, 15]], "Jueves": [[11, 13]]}, 
            {"its": [["Base de datos"]] }),

    Maestro("Contrato 02", "vinculacion", 
            {"miercoles": [[12, 14]], "viernes": [[11, 13]]}, 
            {"its": ["Diseño web"]}),

    Maestro("Contrato 03", "base", 
            {"lunes": [[11, 13]], "miercoles": [[8, 10]]}, 
            {"its": ["Concurrencia y paralelismo"]}),
    
    Maestro("Contrato 04", "tiempo-completo", 
            {"miercoles": [[10, 12]], "viernes": [[13, 15]]}, 
            {"its": ["Sistemas embebidos"]}),
    
    Maestro("Contrato 05", "vinculacion", 
            {"lunes": [[9, 11]], "martes": [[11, 13]]}, 
            {"its": ["Programacion avanzada"]}),
    
    Maestro("Contrato 06", "base", 
            {"martes": [[13, 15]], "jueves": [[7, 9]]}, 
            {"ie": ["Redes de computadoras"]}),
    
    Maestro("Patricia", "tiempo-completo", 
            {"lunes": [[8, 12], [14, 16]], "viernes": [[9, 13], [14, 16]]}, 
            {"ime": ["fisica"], "im": ["quimica"]}),
    
    Maestro("Iván", "vinculacion", 
            {"lunes": [[10, 12], [14, 16]]}, 
            {"ie": ["ingles"], "isc": ["ingles"]}),
    
    Maestro("Adriana", "base", 
            {"martes": [[8, 10], [14, 16]], "jueves": [[7, 9]]}, 
            {"isc": ["calculo"], "its": ["matematicas"]}),
    
    Maestro("César", "tiempo-completo", 
            {"lunes": [[8, 12], [14, 17]], "viernes": [[9, 13], [14, 16]]}, 
            {"ime": ["quimica"], "ie": ["fisica"]}),
   
    Maestro("Teresa", "vinculacion", 
            {"jueves": [[9, 11], [14, 16]]}, 
            {"ime": ["ingles"], "ica": ["ingles"]}),
   
    Maestro("Eduardo", "base",
            {"miercoles": [[9, 11], [13, 15]], "viernes": [[8, 11]]}, 
            {"isc": ["estructuras"], "its": ["calculo"]}),
    
    Maestro("Rosa", "tiempo-completo", 
            {"lunes": [[9, 13], [14, 16]], "jueves": [[9, 12], [14, 17]]}, 
            {"im": ["fisica"], "ime": ["quimica"]}),
    
    Maestro("Julio", "vinculacion", 
            {"martes": [[8, 10]], "viernes": [[10, 12]]}, 
            {"ie": ["ingles"], "isc": ["ingles"]}),
    
    Maestro("Verónica", "base", 
            {"lunes": [[7, 10], [14, 17]], "miercoles": [[9, 11]]}, 
            {"its": ["fisica"], "im": ["quimica"]}),
    
    Maestro("David", "tiempo-completo", 
            {"martes": [[8, 12], [14, 17]], "jueves": [[9, 13], [14, 16]]}, 
            {"isc": ["programacion"], "ie": ["calculo"]}),
    
    Maestro("Cristina", "vinculacion",
            {"jueves": [[9, 11], [14, 16]]}, 
            {"ime": ["ingles"], "ica": ["ingles"]}),
    
    Maestro("José", "base", 
            {"miercoles": [[9, 12], [14, 16]], "viernes": [[8, 11]]}, 
            {"isc": ["matematicas"], "its": ["fisica"]}),
    
    Maestro("Manuel", "tiempo-completo", 
            {"lunes": [[8, 12], [13, 16]], "miercoles": [[7, 10], [12, 14]]}, 
            {"im": ["fisica"], "ime": ["quimica"]}),
    
    Maestro("Gloria", "vinculacion", 
            {"martes": [[9, 11]], "viernes": [[10, 12]]}, 
            {"ie": ["ingles"], "isc": ["ingles"]}),
    
    Maestro("Isabel", "base", 
            {"lunes": [[7, 10], [14, 16]], "jueves": [[8, 11]]}, 
            {"its": ["fisica"], "ime": ["quimica"]}),
    
    Maestro("Pablo", "tiempo-completo", 
            {"miercoles": [[8, 12], [13, 16]], "viernes": [[9, 13]]}, 
            {"isc": ["algoritmos"], "im": ["logica"]}),
]