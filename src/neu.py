import flet as ft


def main(page: ft.Page):
    page.add(
        ft.Stack(
            controls=[
                ft.Container(
                    content=ft.Text("Oben", size=30),
                    bgcolor="blue",
                    padding=20,
                ),
                ft.Container(
                    content=ft.Text("Unten", size=20),
                    bgcolor="red",
                    height=50,
                    bottom=0,  # Setzt den Container exakt an den unteren Rand
                    left=0,
                    right=0,  # Dehnt den Container über die gesamte Breite
                ),
            ],
            expand=True,  # Stack füllt den gesamten Bildschirm aus
        )
    )


ft.app(target=main)
