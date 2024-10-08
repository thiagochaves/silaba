import httpx
import json
import base64
import os
import subprocess
import pyglet

_gabarito = """
{
  "input": {
    "text": "%%%"
  },
  "voice": {
    "languageCode": "pt-BR",
    "name": "pt-BR-Wavenet-D",
    "ssmlGender": "FEMALE"
  },
  "audioConfig": {
    "audioEncoding": "MP3"
  }
}
"""


def texto_para_fala(texto: str):
    if os.path.exists(f"mp3/{ texto }.mp3"):
        return f"mp3/{ texto }.mp3"
    conteúdo_requisição = _gabarito.replace("%%%", texto)
    url = "https://texttospeech.googleapis.com/v1/text:synthesize"
    token_acesso_google = (
        subprocess.run(
            "gcloud auth print-access-token", shell=True, capture_output=True
        )
        .stdout.decode()
        .strip()
    )
    response = httpx.post(
        url,
        json=json.loads(conteúdo_requisição),
        headers={
            "Content-Type": "application/json; charset=utf-8",
            "Authorization": f"Bearer {token_acesso_google}",
            "x-goog-user-project": "silaba-429700",
        },
    )
    conteúdo_resposta = response.json()
    conteúdo_áudio = conteúdo_resposta["audioContent"]
    áudio = base64.b64decode(conteúdo_áudio)
    with open(f"mp3/{ texto }.mp3", "wb") as arquivo:
        arquivo.write(áudio)
    return f"mp3/{ texto }.mp3"


def falar(texto):
    if not texto:
        return
    áudio = texto_para_fala(texto)
    pyglet.media.load(áudio).play()
