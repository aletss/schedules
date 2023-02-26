from dataclasses import dataclass
from calendario import Calendario

@dataclass
class Aula:
    id: int
    calendario: Calendario
    nombre: str = ''

    def reservar_aula(self, materia, bloque):
        # Verifica que el bloque de tiempo no esté ocupado
        if not self.horario.bloque_ocupado(bloque):
            # Agrega el bloque de tiempo al horario del aula
            self.horario.agregar_bloque(bloque)
            print(f"El aula {self.numero} ha sido reservada para {materia} en el bloque de tiempo {bloque}.")
        else:
            print(f"Lo siento, el bloque de tiempo {bloque} ya está ocupado.")
