from dataclasses import dataclass, field
from calendario import Calendario

@dataclass
class Estudiante:
    id: int
    nombre: str
    calendario: Calendario
    id_de_horarios: list = field(default_factory=list) # lista de ids de horarios

    def inscribir_horario(self, horario):
        respuesta = False
        if self.calendario.colisiona_con_bloques(horario.calendario.bloques):
            print(f'El horario es incompatible')

        elif self.id in horario.id_de_estudiantes:
            print(f'{self.nombre} ya está inscrito en el horario')

        else:
            self.id_de_horarios.append(horario.id)
            self.calendario.agregar_bloques(horario.calendario.bloques)
            print(f"{self.nombre} ha inscrito el horario {horario.id} correctamente")
            resuesta = True

        return respuesta
