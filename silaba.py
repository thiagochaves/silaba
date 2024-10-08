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


cor_letra = (0, 149, 255, 255)
cor_fundo = (242, 233, 208, 255)
cor_borda = (0, 0, 204, 30)


def main():
    window = pyglet.window.Window(fullscreen=True)

    @window.event
    def on_draw():
        window.clear()
        pyglet.gl.glClearColor(*[c / 255 for c in cor_fundo])
        draw_bordered_text(
            palavra(),
            window.width // 2,
            window.height // 2,
            border_size=1,
            text_color=cor_letra,
            border_color=cor_borda,
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
