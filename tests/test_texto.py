import pytest

from texto import LIMITE_TEXTO, normalizar_texto_api, transformar_entrada


def test_transformar_entrada_aplica_acentos_conhecidos():
    assert transformar_entrada("cecilia") == "CECÍLIA"


def test_transformar_entrada_ignora_digitos_quando_começa_com_letras():
    assert transformar_entrada("casa12") == "CASA"


def test_transformar_entrada_limita_tamanho():
    assert transformar_entrada("abcdefghijk") == "ABCDEFGHIJ"
    assert len(transformar_entrada("12345678901")) == LIMITE_TEXTO


def test_normalizar_texto_api_rejeita_mistura_de_letras_e_numeros():
    with pytest.raises(ValueError, match="misturar letras e números"):
        normalizar_texto_api("abc123")


def test_normalizar_texto_api_normaliza_minusculas_e_acentos():
    assert normalizar_texto_api("cascão") == "CASCÃO"
