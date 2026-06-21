from Entities.Music import Music
from Repositories.musicRepository import MusicaRepository
from Services.musicService import MusicaService

# Instâncias
repo = MusicaRepository()
service = MusicaService(repo)

# funções para o menu
def exibir_menu():
    print("\n╔══════════════════════════════╗")
    print("║       🎵  AddVibes CLI       ║")
    print("╠══════════════════════════════╣")
    print("║  1 - Listar músicas          ║")
    print("║  2 - Adicionar música        ║")
    print("║  3 - Remover música          ║")
    print("║  0 - Sair                    ║")
    print("╚══════════════════════════════╝")

def listar_musicas():
    musics = service.list_pending_musics()
    if not musics:
        print("\n⚠️  Nenhuma música na fila de pendentes.")
        return
    print(f"\n{'#':<5} {'Nome':<30} {'Artista':<25} {'Pendente'}")
    print("-" * 70)
    for music in musics:
        pendente = "✅ Sim" if music.isPending else "❌ Não"
        print(f"{music.code:<5} {music.name:<30} {music.artist:<25} {pendente}")

def adicionar_musica():
    print("\n── Adicionar música ──")
    nome = input("Nome da música : ").strip()
    
    while not nome:
        print("❌ Nome não pode ser vazio.")
        nome = input("Nome da música : ").strip()

    artista = input("Artista        : ").strip()
    while not artista:
        print("❌ Artista não pode ser vazio.")
        artista = input("Artista        : ").strip()

    nova = Music(name=nome, artist=artista)
    resultado = service.add_music(nova)
    print(f"\n✅ Música adicionada com código #{resultado.code}!")

def remover_musica():
    listar_musicas()
    musics = service.list_pending_musics()
    if not musics:
        return

    print("\n── Remover música ──")
    entrada = input("Digite o código da música a remover: ").strip()

    while not entrada.isdigit():
        print("❌ Código inválido. Digite apenas números.")
        entrada = input("Digite o código da música a remover: ").strip()

    codigo = int(entrada)

    # Verifica se o código existe na lista antes de tentar remover
    codigos_validos = [music.code for music in musics]
    
    if codigo not in codigos_validos:
        print(f"❌ Nenhuma música com código #{codigo} na fila.")
        return

    confirmacao = input(f"Tem certeza que deseja remover a música #{codigo}? (s/n): ").strip().lower()
    
    if confirmacao == "s":
        try:
            service.delete_music(codigo)
            print(f"\n✅ Música #{codigo} removida com sucesso!")
        except Exception as e:
            print(f"\n❌ Erro: {e}")
    else:
        print("Operação cancelada.")

def main():
    print("\nBem-vindo à AddVibes! 🎶")

    while True:
        exibir_menu()
        opcao = input("\nEscolha uma opção: ").strip()

        if opcao == "1":
            listar_musicas()
        elif opcao == "2":
            adicionar_musica()
        elif opcao == "3":
            remover_musica()
        elif opcao == "0":
            print("\nAté logo! 🎵\n")
            break
        else:
            print("❌ Opção inválida. Tente novamente.")

if __name__ == "__main__":
    main()
