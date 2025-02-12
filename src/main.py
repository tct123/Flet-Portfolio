import flet as ft
import colors as cs
import os
from infos import myappbar
from background import mydecoration


def main(page: ft.Page):
    bgcolor = ft.Colors.TRANSPARENT
    global playing
    playing = False
    page.title = "Flet Portfolio"
    page.decoration = mydecoration()
    page.adaptive = True
    page.bgcolor = bgcolor
    page.scroll = True
    page.appbar = myappbar(page=page)
    page.bottom_appbar = ft.BottomAppBar(
        bgcolor=bgcolor,
        content=ft.Row(
            controls=[
                ft.IconButton(icon=ft.Icons.MENU, icon_color=ft.Colors.WHITE),
                ft.Container(expand=True),
            ]
        ),
    )
    page.add(ft.SafeArea(ft.Container()))


ft.app(target=main)
