from dataclasses import dataclass
from calendario import Calendario

@dataclass
class Profesor:
    id: int
    nombre: str
    calendario: Calendario

    def asignar_materia(self, materia, bloque):
        # Verifica que el bloque de tiempo no esté ocupado
        if not self.horario.bloque_ocupado(bloque):
            # Agrega el bloque de tiempo a su horario
            self.horario.agregar_bloque(bloque)
            print(f"{self.nombre} ha sido asignado como profesor de {materia} en el bloque de tiempo {bloque}.")
        else:
            print(f"Lo siento, el bloque de tiempo {bloque} ya está ocupado.")
