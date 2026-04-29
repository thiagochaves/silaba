LIMITE_TEXTO = 10

_SUBSTITUICOES_REMOCAO_ACENTOS = {
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

_SUBSTITUICOES_ADICAO_ACENTOS = {
    "OLIVIA": "OLÍVIA",
    "CECILIA": "CECÍLIA",
    "MARCIA": "MÁRCIA",
    "HELOISA": "HELOÍSA",
    "JOSE": "JOSÉ",
    "MAMAE": "MAMÃE",
    "MAÇA": "MAÇÃ",
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
    "RACAO": "RAÇÃO",
    "PRESEPIO": "PRESÉPIO",
    "PONEI": "PÔNEI",
    "INDIO": "ÍNDIO",
    "XICARA": "XÍCARA",
    "PURE": "PURÊ",
    "IMA": "ÍMÃ",
    "SANSAO": "SANSÃO",
    "MONICA": "MÔNICA",
    "CASCAO": "CASCÃO",
}


def remover_acentos(texto: str) -> str:
    for acento, letra in _SUBSTITUICOES_REMOCAO_ACENTOS.items():
        texto = texto.replace(acento, letra)
    return texto


def adicionar_acentos(texto: str) -> str:
    return _SUBSTITUICOES_ADICAO_ACENTOS.get(texto, texto)


def é_caractere_letra(caractere: str) -> bool:
    if len(caractere) != 1:
        return False
    maiúsculo = caractere.upper()
    sem_acentos = remover_acentos(maiúsculo)
    return maiúsculo == "Ç" or ("A" <= sem_acentos <= "Z")


def normalizar_caractere_letra(caractere: str) -> str:
    maiúsculo = caractere.upper()
    if maiúsculo == "Ç":
        return "Ç"
    return remover_acentos(maiúsculo)


def transformar_entrada(texto: str) -> str:
    resultado = ""
    for caractere in texto:
        if len(resultado) >= LIMITE_TEXTO:
            break
        if caractere.isdigit():
            if not resultado or resultado.isnumeric():
                resultado += caractere
            continue
        if é_caractere_letra(caractere):
            if not resultado or resultado.isalpha():
                resultado += normalizar_caractere_letra(caractere)
                resultado = adicionar_acentos(resultado)
    return resultado


def normalizar_texto_api(texto: str) -> str:
    if not texto:
        raise ValueError("Texto vazio.")
    if len(texto) > LIMITE_TEXTO:
        raise ValueError(f"Texto deve ter no máximo {LIMITE_TEXTO} caracteres.")

    tipos = set()
    for caractere in texto:
        if caractere.isdigit():
            tipos.add("número")
        elif é_caractere_letra(caractere):
            tipos.add("letra")
        else:
            raise ValueError("Texto deve conter apenas letras ou números.")
        if len(tipos) > 1:
            raise ValueError("Texto não pode misturar letras e números.")

    return transformar_entrada(texto)
