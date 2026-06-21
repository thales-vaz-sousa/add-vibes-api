from fastapi import HTTPException
from Entities.Music import Music

class MusicaService:
    def __init__(self, repository):
        self.repository = repository

    def list_pending_musics(self):
        return [music for music in self.repository.list() if music.isPending]

    def add_music(self, music: Music):
        return self.repository.add(music)

    def delete_music(self, code: int):
        success = self.repository.remove(code)
        if not success:
            raise HTTPException(status_code=404, detail="Música não encontrada na lista de pendentes.")
        return {"detail": "Música eliminada com sucesso da fila."}