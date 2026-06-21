from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from Controllers.musicController import router as music_router
from scalar_fastapi import get_scalar_api_reference

api = FastAPI(title="AddVibes API", docs_url=None)

# interceptar chamadas a api
api.add_middleware(
    CORSMiddleware,
    allow_origins=["http://localhost:4200", "https://localhost:4200"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

api.include_router(music_router)

#documentação da api (verificar endpoints etc...)
@api.get("/docs", include_in_schema=False)
async def scalar_html():
    return get_scalar_api_reference(
        openapi_url=api.openapi_url,
        title=api.title,
        show_sidebar=True,
        hide_client_button=True,
        show_developer_tools="never",
        overrides={"agent": {"disabled": True},"theme": {"default": "purple"}},
    )

@api.get("/", tags=["Root"])
def root():
    return {"message": "Bem-vindo à AddVibes-Api!"}

app = api  # alias para o Render encontrar

if __name__ == "__main__":
    import uvicorn
    uvicorn.run("main:api", host="127.0.0.1", port=8000, reload=True)