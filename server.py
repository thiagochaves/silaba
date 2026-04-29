from pathlib import Path

from fastapi import FastAPI, HTTPException
from fastapi.responses import FileResponse

from speech import obter_mp3
from texto import normalizar_texto_api


_BASE_DIR = Path(__file__).resolve().parent
_INDEX_PATH = _BASE_DIR / "static" / "index.html"
_APP_JS_PATH = _BASE_DIR / "static" / "app.js"

app = FastAPI(title="silaba")


@app.get("/", include_in_schema=False)
def index() -> FileResponse:
    return FileResponse(_INDEX_PATH)


@app.get("/app.js", include_in_schema=False)
def app_js() -> FileResponse:
    return FileResponse(_APP_JS_PATH, media_type="application/javascript")


@app.get("/api/audio/{texto}")
def audio(texto: str) -> FileResponse:
    try:
        texto_normalizado = normalizar_texto_api(texto)
    except ValueError as erro:
        raise HTTPException(status_code=400, detail=str(erro)) from erro

    try:
        caminho_mp3 = obter_mp3(texto_normalizado)
    except Exception as erro:
        raise HTTPException(
            status_code=502,
            detail="Falha ao gerar o áudio.",
        ) from erro

    return FileResponse(
        caminho_mp3,
        media_type="audio/mpeg",
        filename=f"{texto_normalizado}.mp3",
    )
