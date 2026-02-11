import flet as ft


def mybutton(page, text: str, on_click, disabled: bool = False):
    return ft.Button(
        adaptive=True,
        content=ft.Text(text, size=20),
        height=50,
        expand=True,  # Automatische Anpassung der Breite
        on_click=on_click,
        disabled=disabled,
        style=ft.ButtonStyle(
            bgcolor={
                ft.ControlState.DEFAULT: ft.Colors.RED,
                ft.ControlState.PRESSED: ft.Colors.TRANSPARENT,
            },
            shape=ft.RoundedRectangleBorder(radius=10),
        ),
    )
