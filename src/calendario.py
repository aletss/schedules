from dataclasses import dataclass, field
import config
from datetime import datetime


@dataclass
class BloqueDeTiempo:
    # 0-6 domingo a sabado
    dia: int
    # número de periodo. Esto se puede interpretar como hora del dia, media hora del dia, 15 min, etc. 
    # Ejemplo 0-23 para 24 horas donde 0 representa de las 00:00 a las 01:00 hrs
    periodo: int
    # Titulo / descripcion de evento
    descripcion: str = ''

    def __post_init__(self):
        if not isinstance(self.dia, int):
            raise TypeError("Valor para el atributo dia debe ser entero")
        if self.dia < 0 or self.dia >= config.DIAS:
            raise ValueError(f"Valor para el atributo dia debe estar entre {0} y {DIAS-1}")
        
        if not isinstance(self.periodo, int):
            raise TypeError("Valor para el atributo periodo debe ser entero")
        if self.periodo < 0 or self.periodo >= config.PERIODOS:
            raise ValueError(f"Valor para el atributo dia debe estar entre {0} y {PERIODO-1}")


    def colisiona_con(self, otro_bloque):
        if (self.dia, self.periodo) == (otro_bloque.dia, otro_bloque.periodo):
            return True
        else:
            return False

    def __str__(self):
        return f"(Dia {self.dia}, Periodo {self.periodo}) - {self.descripcion}"

@dataclass
class Calendario:
    bloques: list = field(default_factory=list)

    def __post_init__(self):
        for bloque in self.bloques:
            if not isinstance(bloque, BloqueDeTiempo):
                raise TypeError(f"El objeto {bloque} no es un BloqueDeTiempo")

    def agregar_bloques(self, bloques_externos):
        if self.colisiona_con_bloques(bloques_externos):
            print('bloques incompatibles')
        else:
            for bloque_externo in bloques_externos:
                self.bloques.append(bloque_externo)

    def imprimir(self):
        for bloque in self.bloques:
            print(bloque)

    def colisiona_con_bloques(self, lista_bloques):
        for bloque_1 in self.bloques:
            for bloque_2 in lista_bloques:
                if bloque_1.colisiona_con(bloque_2):
                    print(f'Bloque {bloque_1} colisiona con bloque {bloque_2}')
                    return True
        return False
