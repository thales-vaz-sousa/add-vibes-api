# 🎵 AddVibes — Como rodar o projeto

## Pré-requisitos

Antes de qualquer coisa, certifique-se de ter instalado:

- [Python 3.10+](https://www.python.org/downloads/)
- pip (já vem com o Python)

---

## 1. Clonar / baixar o projeto

Se estiver usando Git:

```bash
git clone <url-do-repositorio>
cd addvibes
```

Ou simplesmente extraia o `.zip` do projeto e abra a pasta no terminal.

---

## 2. Instalar as dependências

```bash
pip install fastapi uvicorn pydantic scalar-fastapi
```

> ```bash
> python -m venv venv
>
> # Windows
> venv\Scripts\activate
>
> # Linux / macOS
> source venv/bin/activate
> ```

---

## 3. Estrutura esperada do projeto

Certifique-se de que os arquivos estão organizados assim:

```
addvibes/
├── main.py
├── cli.py
├── Entities/
│   └── Music.py
├── Repositories/
│   └── musicRepository.py
├── Services/
│   └── musicService.py
└── Controllers/
    └── musicController.py
```

---

## ▶️ Opção A — Rodar o CLI (menu interativo)

```bash
python cli.py
```

Você verá o menu abaixo no terminal:

```
╔══════════════════════════════╗
║       🎵  AddVibes CLI        ║
╠══════════════════════════════╣
║  1 - Listar músicas          ║
║  2 - Adicionar música        ║
║  3 - Remover música          ║
║  0 - Sair                    ║
╚══════════════════════════════╝
```

Use os números para navegar. Os dados ficam salvos **enquanto o programa estiver aberto**.

---

## ▶️ Opção B — Rodar a API (FastAPI)

```bash
python main.py
```

A API subirá em: **http://127.0.0.1:8000**

### Endpoints disponíveis

| Método | Rota              | Descrição                        |
|--------|-------------------|----------------------------------|
| GET    | `/`               | Mensagem de boas-vindas          |
| GET    | `/musicas`        | Lista músicas pendentes          |
| POST   | `/musicas`        | Adiciona uma música              |
| DELETE | `/musicas/{code}` | Remove uma música pelo código    |

### Documentação interativa

Acesse **http://127.0.0.1:8000/docs** no navegador para testar os endpoints visualmente.

### Exemplo de requisição POST

```json
{
  "name": "Bohemian Rhapsody",
  "artist": "Queen"
}
```

---

## ❓ Erros comuns

**`ModuleNotFoundError: No module named 'fastapi'`**
→ Rode `pip install fastapi uvicorn pydantic scalar-fastapi` novamente.

**`ModuleNotFoundError: No module named 'Entities'`**
→ Verifique se está rodando o comando **a partir da pasta raiz do projeto** (onde fica o `main.py` e o `cli.py`).

**Porta 8000 já em uso**
→ Encerre o processo que está usando a porta ou altere a porta no `main.py`:
```python
uvicorn.run("main:api", host="127.0.0.1", port=8080, reload=True)
```
