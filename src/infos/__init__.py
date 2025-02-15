import flet as ft


def myappbar(title, bgcolor, items: list):
    return ft.AppBar(
        title=ft.Text(title),
        center_title=True,
        adaptive=True,
        bgcolor=bgcolor,
        actions=[
            ft.PopupMenuButton(
                bgcolor=bgcolor,
                items=items,
            )
        ],
    )
