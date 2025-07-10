import flet as ft


def mybutton(page, text: str, on_click, disabled: bool = False):
    return ft.ElevatedButton(
        adaptive=True,
        content=ft.Text(text, size=20),
        height=50,
        expand=True,  # Automatische Anpassung der Breite
        on_click=on_click,
        bgcolor={
            ft.ControlState.DEFAULT: ft.Colors.RED,
            ft.ControlState.PRESSED: ft.Colors.TRANSPARENT,
        },
        disabled=disabled,
        style=ft.ButtonStyle(shape=ft.RoundedRectangleBorder(radius=10)),
    )
