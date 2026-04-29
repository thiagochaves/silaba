from texto import (
    LIMITE_TEXTO,
    adicionar_acentos as _adicionar_acentos,
    normalizar_caractere_letra,
    remover_acentos as _remover_acentos,
)


_palavra = ""
_mudou = False


def mudou():
    global _mudou
    try:
        return _mudou
    finally:
        _mudou = False


def palavra():
    return _palavra


def apagar():
    global _palavra, _mudou
    _palavra = _remover_acentos(_palavra[:-1])
    _mudou = True


def apagar_tudo():
    global _palavra, _mudou
    _palavra = ""
    _mudou = True


def remover_acentos(palavra):
    return _remover_acentos(palavra)


def adicionar(symbol):
    global _palavra, _mudou
    if len(_palavra) >= LIMITE_TEXTO:
        return
    if len(_palavra) == 0 or _palavra.isalpha():
        _palavra += "Ç" if symbol == 201863462912 else normalizar_caractere_letra(chr(symbol))
        _palavra = _adicionar_acentos(_palavra)
        _mudou = True


def adicionar_número(symbol):
    global _palavra, _mudou
    if len(_palavra) >= LIMITE_TEXTO:
        return
    # Somente adiciona um número se a _palavra estiver vazia ou for composta somente de números
    if len(_palavra) == 0 or _palavra.isnumeric():
        _palavra += chr(symbol)
        _mudou = True


def adicionar_acentos(palavra):
    return _adicionar_acentos(palavra)


def é_letra(symbol):
    return 65 <= symbol <= 90 or 97 <= symbol <= 122 or symbol == 201863462912


def é_número(symbol):
    return 48 <= symbol <= 57
