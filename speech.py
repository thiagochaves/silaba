import os
from collections.abc import Callable
from pathlib import Path

from speech_google import sintetizar_mp3 as sintetizar_mp3_google
from speech_gtts import sintetizar_mp3 as sintetizar_mp3_gtts


_CACHE_DIR = Path(__file__).resolve().parent / "mp3"
_BACKEND_PADRAO = "gtts"


def caminho_mp3(texto: str) -> Path:
    return _CACHE_DIR / f"{texto}.mp3"


def backend_tts() -> str:
    return os.getenv("SILABA_TTS_BACKEND", _BACKEND_PADRAO).strip().lower()


def _ordem_de_backends() -> list[tuple[str, Callable[[str], bytes]]]:
    preferido = backend_tts()
    if preferido == "google":
        return [
            ("google", sintetizar_mp3_google),
            ("gtts", sintetizar_mp3_gtts),
        ]
    return [
        ("gtts", sintetizar_mp3_gtts),
        ("google", sintetizar_mp3_google),
    ]


def sintetizar_mp3(texto: str) -> bytes:
    erros = []
    for nome, sintetizador in _ordem_de_backends():
        try:
            return sintetizador(texto)
        except Exception as erro:
            erros.append(f"{nome}: {erro}")
    raise RuntimeError("Falha ao gerar MP3. " + " | ".join(erros))


def obter_mp3(texto: str) -> Path:
    caminho = caminho_mp3(texto)
    if caminho.exists():
        return caminho

    caminho.parent.mkdir(exist_ok=True)
    caminho.write_bytes(sintetizar_mp3(texto))
    return caminho
