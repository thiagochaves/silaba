import pyglet

from speech import obter_mp3


def texto_para_fala(texto: str):
    return str(obter_mp3(texto))


def falar(texto):
    if not texto:
        return
    áudio = texto_para_fala(texto)
    pyglet.media.load(áudio).play()
