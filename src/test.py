from calendario import Calendario, BloqueDeTiempo
from estudiante import Estudiante
from profesor import Profesor
from materia import Materia
from aula import Aula
from horario import Clase, Horario

# Entidades
materia_1 = Materia(id = 1, nombre = 'Geometría', preriodos_semanales = 10)
profesor_1 = Profesor(id = 1, nombre = 'Rulo', calendario = Calendario())
aula_1 = Aula(id = 1, nombre = 'A 401', calendario = Calendario())
estudiante_1 = Estudiante(id = 1, nombre = 'Carlos', calendario = Calendario())

# Horario de clase geometría
clase_1 = Clase(aula_id = aula_1.id
    , profesor_id = profesor_1.id
    , materia_id = materia_1.id
    , bloque = BloqueDeTiempo(dia=1, periodo=1)
)
clase_2 = Clase(aula_id = aula_1.id
    , profesor_id = profesor_1.id
    , materia_id = materia_1.id
    , bloque = BloqueDeTiempo(dia=1, periodo=2)
)
horario_1 = Horario(id = 1, calendario = Calendario(), clases = [clase_1, clase_2])


# Inscripciones



respuesta = estudiante_1.inscribir_horario(horario_1)
if respuesta:
    horario_1.agregar_estudiante_id(estudiante_1.id)



# Horario de clase probabilidad
profesor_2 = Profesor(id = 2, nombre = 'Coca', calendario = Calendario())
materia_2 = Materia(id = 2, nombre = 'Probabilidad', preriodos_semanales = 10)

clase_3 = Clase(aula_id = aula_1.id
    , profesor_id = profesor_2.id
    , materia_id = materia_2.id
    , bloque = BloqueDeTiempo(dia=2, periodo=4)
)
clase_4 = Clase(aula_id = aula_1.id
    , profesor_id = profesor_2.id
    , materia_id = materia_2.id
    , bloque = BloqueDeTiempo(dia=2, periodo=5)
)
horario_2 = Horario(id = 2, calendario = Calendario(), clases = [clase_3, clase_4])

respuesta = estudiante_1.inscribir_horario(horario_2)
if respuesta:
    horario_2.agregar_estudiante_id(estudiante_1.id)
