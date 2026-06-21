from fastapi import APIRouter
from Entities.Music import Music 
from Repositories.musicRepository import MusicaRepository
from Services.musicService import MusicaService

router = APIRouter(
    prefix="/musicas",
    tags=["Controller"]  
)

#Instancias
musica_repo = MusicaRepository()
musica_service = MusicaService(musica_repo)

#Rotas
@router.get("")  
def listar_musicas():
    """Listar Músicas Pendentes"""
    return musica_service.list_pending_musics()

@router.post("")
def adicionar_musica(musica: Music):
    """Adicionar música à lista de pendentes"""
    return musica_service.add_music(musica) 

@router.delete("/{codigo}")
def eliminar_musica(codigo: int):
    """Eliminar música na lista de pendentes"""
    return musica_service.delete_music(codigo)