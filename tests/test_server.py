from pathlib import Path

from fastapi.testclient import TestClient

import server


client = TestClient(server.app)


def test_index_retorna_html():
    resposta = client.get("/")

    assert resposta.status_code == 200
    assert "text/html" in resposta.headers["content-type"]
    assert 'id="entrada"' in resposta.text
    assert '/static/ComicNeue-Regular.ttf' in resposta.text


def test_static_retorna_fonte():
    resposta = client.get("/static/ComicNeue-Regular.ttf")

    assert resposta.status_code == 200
    assert resposta.content


def test_audio_retorna_mp3_cacheado(monkeypatch, tmp_path: Path):
    caminho = tmp_path / "OLA.mp3"
    caminho.write_bytes(b"audio")

    def falso_obter_mp3(texto: str) -> Path:
        assert texto == "OLA"
        return caminho

    monkeypatch.setattr(server, "obter_mp3", falso_obter_mp3)

    resposta = client.get("/api/audio/ola")

    assert resposta.status_code == 200
    assert resposta.content == b"audio"
    assert resposta.headers["content-type"] == "audio/mpeg"


def test_audio_rejeita_texto_misto():
    resposta = client.get("/api/audio/ola123")

    assert resposta.status_code == 400
    assert resposta.json()["detail"] == "Texto não pode misturar letras e números."


def test_audio_retorna_erro_quando_tts_falha(monkeypatch):
    def falso_obter_mp3(_: str):
        raise RuntimeError("falhou")

    monkeypatch.setattr(server, "obter_mp3", falso_obter_mp3)

    resposta = client.get("/api/audio/ola")

    assert resposta.status_code == 502
    assert resposta.json()["detail"] == "Falha ao gerar o áudio."
