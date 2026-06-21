from typing import Dict, List
from Entities.Music import Music

class MusicaRepository:
    def __init__(self):
        self.listaDeMusicas: Dict[int, Music] = {}
        self.ultimo_codigo = 0  # Contador automático

    def list(self) -> List[Music]:
        return list(self.listaDeMusicas.values())

    def add(self, musica: Music) -> Music:
        # Incrementa o código automaticamente
        self.ultimo_codigo += 1
        musica.code = self.ultimo_codigo
        
        # Salva no dicionário usando o novo código gerado
        self.listaDeMusicas[musica.code] = musica
        return musica

    def remove(self, codigo: int) -> bool:
        if codigo in self.listaDeMusicas:
            del self.listaDeMusicas[codigo]
            return True
        return False