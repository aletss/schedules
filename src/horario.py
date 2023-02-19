from dataclasses import dataclass, field
from calendario import Calendario, BloqueDeTiempo
from aula import Aula
from profesor import Profesor
from materia import Materia

@dataclass
class Clase:
    aula_id: int
    profesor_id: int
    materia_id: int
    bloque: BloqueDeTiempo

    def actualizar_descripcion(self):
        self.bloque.descripcion = (
            f'Profesor: {self.profesor_id}\n'
            f'Materia: {self.materia_id}\n'
            f'Aula: {self.aula_id}\n'
            )
        
    def __post_init__(self):
        self.actualizar_descripcion()
        
@dataclass
class Horario:
    id: int
    clases: list[Clase]
    calendario: Calendario
    id_de_estudiantes: list = field(default_factory=list)

    def agregar_clase(self, nueva_clase):
        if self.calendario.colisiona_con_bloques([nueva_clase.bloque]):
            print('Bloque ya está ocupado')
        else:
            self.calendario.agregar_bloques([nueva_clase.bloque])
            self.clases.append(nueva_clase)

    def __post_init__(self):
        print(self.calendario)
        for clase in self.clases:
            self.calendario.agregar_bloques([clase.bloque])

    def agregar_estudiante(self, estudiante_id):
        self.id_de_estudiantes.append(estudiante_id)

