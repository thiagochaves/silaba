# nmap <leader>0 :!uv run %<CR>

import pyglet
import fala

label = None
palavra = None
mudou = False


azul = (0, 149, 255, 255)


# Function to draw bordered text
def draw_bordered_text(
    text,
    x,
    y,
    border_size=2,
    text_color=(255, 255, 255, 255),
    border_color=(0, 0, 0, 255),
):
    # Create the label for the text
    label = pyglet.text.Label(
        text,
        font_name="Comic Neue",
        font_size=180,
        x=x,
        y=y,
        anchor_x="center",
        anchor_y="center",
        color=text_color,
    )

    # Draw the border by drawing the label slightly offset in 8 directions (like a shadow effect)
    offsets = [
        (-border_size, -border_size),
        (-border_size, 0),
        (-border_size, border_size),
        (0, -border_size),
        (0, border_size),
        (border_size, -border_size),
        (border_size, 0),
        (border_size, border_size),
    ]

    for dx, dy in offsets:
        border_label = pyglet.text.Label(
            text,
            font_name="Comic Neue",
            font_size=180,
            x=x + dx,
            y=y + dy,
            anchor_x="center",
            anchor_y="center",
            color=border_color,
        )
        border_label.draw()

    # Draw the actual text on top of the border
    label.draw()


def main():
    global label, palavra
    window = pyglet.window.Window(fullscreen=True)
    label = pyglet.text.Label(
        "Sílaba",
        font_name="Comic Neue",
        font_size=180,
        x=window.width // 2,
        y=window.height // 2,
        anchor_x="center",
        anchor_y="center",
        color=(0, 149, 255),
    )
    palavra = ""
    label.text = palavra

    @window.event
    def on_draw():
        global mudou, palavra
        window.clear()
        # label.draw()
        draw_bordered_text(
            palavra,
            window.width // 2,
            window.height // 2,
            text_color=azul,
            border_color=(255, 255, 255, 255),
        )
        if mudou:
            fala.falar(palavra)
            mudou = False

    @window.event
    def on_key_press(symbol, modifiers):
        # print(f"Símbolo: {symbol}")
        if symbol == pyglet.window.key.ESCAPE:
            window.close()
        elif symbol == pyglet.window.key.BACKSPACE:
            apagar()
        elif symbol == pyglet.window.key.RETURN:
            fala.falar(palavra)
        elif symbol == pyglet.window.key.DELETE or symbol == pyglet.window.key.SPACE:
            apagar_tudo()
        elif é_letra(symbol):
            adicionar(symbol)
        elif é_número(symbol):
            adicionar_número(symbol)

    pyglet.app.run()


def apagar():
    global palavra, label, mudou
    palavra = remover_acentos(palavra[:-1])
    label.text = palavra
    mudou = True


def apagar_tudo():
    global palavra, label, mudou
    palavra = ""
    label.text = palavra
    mudou = True


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
    global palavra, label, mudou
    if len(palavra) >= 10:
        return
    if len(palavra) == 0 or palavra.isalpha():
        palavra += chr(symbol).upper() if symbol != 201863462912 else "Ç"
        palavra = adicionar_acentos(palavra)
        label.text = palavra
        mudou = True


def adicionar_número(symbol):
    global palavra, label, mudou
    if len(palavra) >= 10:
        return
    # Somente adiciona um número se a palavra estiver vazia ou for composta somente de números
    if len(palavra) == 0 or palavra.isnumeric():
        palavra += chr(symbol)
        label.text = palavra
        mudou = True


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


if __name__ == "__main__":
    main()
