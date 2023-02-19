from dataclasses import dataclass, field

@dataclass
class Escuela:
    estudiantes: list
    profesores: list
    materias: list
    aulas: list
    horarios: list = field(default_factory=list)
