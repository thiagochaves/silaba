import httpx
import json
import base64
import os
import subprocess
import pyglet
from google.cloud import texttospeech


_cliente = texttospeech.TextToSpeechClient()


def texto_para_fala(texto: str):
    if os.path.exists(f"mp3/{ texto }.mp3"):
        return f"mp3/{ texto }.mp3"
    input = texttospeech.SynthesisInput(text=texto)
    voz = texttospeech.VoiceSelectionParams(
        language_code="pt-BR",
        ssml_gender=texttospeech.SsmlVoiceGender.FEMALE,
        name="pt-BR-Wavenet-D",
    )
    configuração_áudio = texttospeech.AudioConfig(
        audio_encoding=texttospeech.AudioEncoding.MP3,
        pitch=0.0,
        speaking_rate=1.0,
    )
    resposta = _cliente.synthesize_speech(
        input=input,
        voice=voz,
        audio_config=configuração_áudio,
    )
    áudio = resposta.audio_content
    with open(f"mp3/{ texto }.mp3", "wb") as arquivo:
        arquivo.write(áudio)
    return f"mp3/{ texto }.mp3"


def falar(texto):
    if not texto:
        return
    áudio = texto_para_fala(texto)
    pyglet.media.load(áudio).play()
