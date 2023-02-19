from escuela import Escuela
from estudiante import Estudiante
from calendario import Calendario
from materia import Materia
from aula import Aula

n_estudiantes = 7*40 # 7 grupos de 40 personas
n_profesores = 20
n_aulas = 10
n_horarios = 7*7 # 7 materias para cada uno de los 7 grupos
periodos_por_dia = 24 # periodos = hora

# simular estudiantes
estudiantes = []
for i in range(n_estudiantes):
    estudiantes.append(
        Estudiante(id=i, nombre=f'estudiante {i}', calendario=Calendario())
    )

# simular profesores
profesores = []
for i in range(n_profesores):
    profesores.append(
        Estudiante(id=i, nombre=f'profesor {i}', calendario=Calendario())
    )

# simular materias
materias = [
    Materia(id=0, periodos_semanales=6, nombre='Algebra Superior I')
    , Materia(id=1, periodos_semanales=8, nombre='Cálculo Diferencial e Integral I')
    , Materia(id=2, periodos_semanales=4, nombre='Geometría I')
    , Materia(id=3, periodos_semanales=6, nombre='Algoritmos y Programación')
    , Materia(id=4, periodos_semanales=4, nombre='Seguro de Vida')
]

# simular aulas
aulas = []
for i in range(n_aulas):    
    aulas.append(
        Aula(id=i, nombre=f'aula {i}', calendario=Calendario())
    )


actuaria_semestre_1 = Escuela(
    estudiantes = estudiantes
    , profesores = profesores
    , materias = materias
    , aulas = aulas
)

print(actuaria_semestre_1)

# simular horarios
horarios = []
