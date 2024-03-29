import reflex as rx
from color_picker import color_picker

def index() -> rx.Component:
    picker = color_picker()
    return rx.center(
        rx.hstack(
            rx.vstack(
                rx.input(value=picker.color, on_change=picker.State.set_color),
                rx.heading(picker.color, color=picker.color),
                picker
            ),
        ),
        height="100vh"
    )


# Add state and page to the app.
app = rx.App()
app.add_page(index)
