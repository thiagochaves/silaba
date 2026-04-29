from pathlib import Path

import pytest

import speech


def test_obter_mp3_retorna_cache_sem_chamar_backend(monkeypatch, tmp_path: Path):
    caminho = tmp_path / "OLA.mp3"
    caminho.write_bytes(b"cache")

    monkeypatch.setattr(speech, "caminho_mp3", lambda _: caminho)
    monkeypatch.setattr(
        speech,
        "sintetizar_mp3_gtts",
        lambda _: pytest.fail("gTTS não deveria ser chamado"),
    )
    monkeypatch.setattr(
        speech,
        "sintetizar_mp3_google",
        lambda _: pytest.fail("Google não deveria ser chamado"),
    )

    assert speech.obter_mp3("OLA") == caminho


def test_sintetizar_mp3_usa_gtts_por_padrao(monkeypatch):
    monkeypatch.delenv("SILABA_TTS_BACKEND", raising=False)
    monkeypatch.setattr(speech, "sintetizar_mp3_gtts", lambda _: b"gtts")
    monkeypatch.setattr(
        speech,
        "sintetizar_mp3_google",
        lambda _: pytest.fail("Google não deveria ser chamado"),
    )

    assert speech.sintetizar_mp3("OLA") == b"gtts"


def test_sintetizar_mp3_faz_fallback_para_google(monkeypatch):
    monkeypatch.delenv("SILABA_TTS_BACKEND", raising=False)

    def falha_gtts(_: str) -> bytes:
        raise RuntimeError("sem conexão")

    monkeypatch.setattr(speech, "sintetizar_mp3_gtts", falha_gtts)
    monkeypatch.setattr(speech, "sintetizar_mp3_google", lambda _: b"google")

    assert speech.sintetizar_mp3("OLA") == b"google"


def test_sintetizar_mp3_respeita_backend_google_forcado(monkeypatch):
    monkeypatch.setenv("SILABA_TTS_BACKEND", "google")
    monkeypatch.setattr(speech, "sintetizar_mp3_google", lambda _: b"google")
    monkeypatch.setattr(
        speech,
        "sintetizar_mp3_gtts",
        lambda _: pytest.fail("gTTS não deveria ser chamado antes do Google"),
    )

    assert speech.sintetizar_mp3("OLA") == b"google"


def test_sintetizar_mp3_falha_quando_todos_os_backends_falham(monkeypatch):
    monkeypatch.delenv("SILABA_TTS_BACKEND", raising=False)

    monkeypatch.setattr(
        speech,
        "sintetizar_mp3_gtts",
        lambda _: (_ for _ in ()).throw(RuntimeError("gtts falhou")),
    )
    monkeypatch.setattr(
        speech,
        "sintetizar_mp3_google",
        lambda _: (_ for _ in ()).throw(RuntimeError("google falhou")),
    )

    with pytest.raises(RuntimeError, match="gtts: gtts falhou"):
        speech.sintetizar_mp3("OLA")
