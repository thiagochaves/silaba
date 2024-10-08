# nmap <leader>0 :!uv run %<CR>

import pyglet
import fala
from render import draw_bordered_text
from palavra import (
    palavra,
    apagar,
    apagar_tudo,
    adicionar,
    adicionar_número,
    é_letra,
    é_número,
    mudou,
)


azul = (0, 149, 255, 255)


def main():
    window = pyglet.window.Window(fullscreen=True)

    @window.event
    def on_draw():
        window.clear()
        draw_bordered_text(
            palavra(),
            window.width // 2,
            window.height // 2,
            text_color=azul,
            border_color=(255, 255, 255, 255),
        )
        if mudou():
            fala.falar(palavra())

    @window.event
    def on_key_press(symbol, modifiers):
        # print(f"Símbolo: {symbol}")
        if symbol == pyglet.window.key.ESCAPE:
            window.close()
        elif symbol == pyglet.window.key.BACKSPACE:
            apagar()
        elif symbol == pyglet.window.key.RETURN:
            fala.falar(palavra())
        elif symbol == pyglet.window.key.DELETE or symbol == pyglet.window.key.SPACE:
            apagar_tudo()
        elif é_letra(symbol):
            adicionar(symbol)
        elif é_número(symbol):
            adicionar_número(symbol)

    pyglet.app.run()


if __name__ == "__main__":
    main()
