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
    _palavra = remover_acentos(_palavra[:-1])
    _mudou = True


def apagar_tudo():
    global _palavra, _mudou
    _palavra = ""
    _mudou = True


def remover_acentos(palavra):
    substituições = {
        "Á": "A",
        "À": "A",
        "Ã": "A",
        "Â": "A",
        "É": "E",
        "Ê": "E",
        "Í": "I",
        "Ó": "O",
        "Ô": "O",
        "Õ": "O",
        "Ú": "U",
        "Ç": "C",
    }
    for acento, letra in substituições.items():
        palavra = palavra.replace(acento, letra)
    return palavra


def adicionar(symbol):
    global _palavra, _mudou
    if len(_palavra) >= 10:
        return
    if len(_palavra) == 0 or _palavra.isalpha():
        _palavra += chr(symbol).upper() if symbol != 201863462912 else "Ç"
        _palavra = adicionar_acentos(_palavra)
        _mudou = True


def adicionar_número(symbol):
    global _palavra, _mudou
    if len(_palavra) >= 10:
        return
    # Somente adiciona um número se a _palavra estiver vazia ou for composta somente de números
    if len(_palavra) == 0 or _palavra.isnumeric():
        _palavra += chr(symbol)
        _mudou = True


def adicionar_acentos(palavra):
    substituições = {
        "OLIVIA": "OLÍVIA",
        "CECILIA": "CECÍLIA",
        "MARCIA": "MÁRCIA",
        "HELOISA": "HELOÍSA",
        "JOSE": "JOSÉ",
        "MAMAE": "MAMÃE",
        "SAO": "SÃO",
        "NAO": "NÃO",
        "AGUA": "ÁGUA",
        "ARVORE": "ÁRVORE",
        "AVIAO": "AVIÃO",
        "AVO": "AVÔ",
        "BOTAO": "BOTÃO",
        "BEBE": "BEBÊ",
        "CARIE": "CÁRIE",
        "CHA": "CHÁ",
        "CEU": "CÉU",
        "CORACAO": "CORAÇÃO",
        "FACIL": "FÁCIL",
        "FOSFORO": "FÓSFORO",
        "LAPIS": "LÁPIS",
        "MACA": "MAÇÃ",
        "MAO": "MÃO",
        "IRMAO": "IRMÃO",
        "IRMA": "IRMÃ",
        "PE": "PÉ",
        "PAO": "PÃO",
        "PESSEGO": "PÊSSEGO",
        "RAPIDO": "RÁPIDO",
        "SABADO": "SÁBADO",
        "TENIS": "TÊNIS",
        "VOVO": "VOVÓ",
        "VOCE": "VOCÊ",
        "MUSICA": "MÚSICA",
        "HISTORIA": "HISTÓRIA",
        "MAGICO": "MÁGICO",
        "AGUIA": "ÁGUIA",
        "ONIBUS": "ÔNIBUS",
        "TELEVISAO": "TELEVISÃO",
        "BALAO": "BALÃO",
        "ALGODAO": "ALGODÃO",
        "TUNEL": "TÚNEL",
        "LEAO": "LEÃO",
        "PO": "PÓ",
        "NATACAO": "NATAÇÃO",
        "ABOBORA": "ABÓBORA",
        "ANAO": "ANÃO",
        "CAMALEAO": "CAMALEÃO",
        "ESCORPIAO": "ESCORPIÃO",
        "ESPIAO": "ESPIÃO",
        "AVIAOZINHO": "AVIÃOZINHO",
        "DEDAO": "DEDÃO",
        "CHAO": "CHÃO",
        "VIOLAO": "VIOLÃO",
        "BOLAOZINHO": "BALÃOZINHO",
        "CANCAO": "CANÇÃO",
        "DRAGAO": "DRAGÃO",
        "FOGAO": "FOGÃO",
        "LEAOZINHO": "LEÃOZINHO",
        "MAOZINHA": "MÃOZINHA",
        "FAISCA": "FAÍSCA",
        "CANCAO": "CANÇÃO",
        "RACAO": "RAÇÃO",
        "PRESEPIO": "PRESÉPIO",
        "PONEI": "PÔNEI",
        "INDIO": "ÍNDIO",
        "XICARA": "XÍCARA",
        "PURE": "PURÊ",
    }
    if palavra in substituições:
        return substituições[palavra]
    return palavra


def é_letra(symbol):
    return 65 <= symbol <= 90 or 97 <= symbol <= 122 or symbol == 201863462912


def é_número(symbol):
    return 48 <= symbol <= 57
