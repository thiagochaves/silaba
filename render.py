import pyglet

_FONTE = "Comic Neue"


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
        font_name=_FONTE,
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
            font_name=_FONTE,
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
