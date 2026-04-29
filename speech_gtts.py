from io import BytesIO

from gtts import gTTS


def sintetizar_mp3(texto: str) -> bytes:
    buffer = BytesIO()
    tts = gTTS(text=texto, lang="pt", tld="com.br")
    tts.write_to_fp(buffer)
    return buffer.getvalue()
