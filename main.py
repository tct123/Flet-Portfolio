import flet as ft
from flet_contrib.color_picker import *
from flet_contrib.flexible_slider import *
from flet_contrib.shimmer import *
from flet_contrib.vertical_splitter import *
import colors as cs
import openweb as ob
import os

bgcolor = cs.RED
btnlist = ["1", "2"]


def main(page: ft.Page):
    page.title = "Portfolio"
    page.adaptive = True
    # page.bgcolor = bgcolor
    music = ft.Audio(src=f"{os.getcwd()}/assets/mozart.mp3", autoplay=True)
    page.overlay.append(music)
    page.scroll = True

    def opengithub(e):
        ob.openweb(e=e, page=page, url="https://github.com/tct123")

    def openyt1(e):
        ob.openweb(e=e, page=page, url="https://youtube.com/@tc-diy")

    page.appbar = ft.AppBar(
        title=ft.Text(page.title),
        center_title=True,
        bgcolor=bgcolor,
        adaptive=True,
        actions=[
            ft.PopupMenuButton(
                items=[
                    ft.PopupMenuItem(
                        icon=ft.icons.CLOUD, text="Github", on_click=opengithub
                    ),
                    ft.PopupMenuItem(
                        icon=ft.icons.PLAY_CIRCLE, text="YouTube", on_click=openyt1
                    ),
                ]
            )
        ],
    )
    page.bottom_appbar = ft.BottomAppBar(
        content=ft.Row(
            controls=[
                ft.IconButton(icon=ft.icons.MENU, icon_color=ft.colors.WHITE),
                ft.Container(expand=True),
            ]
        ),
        bgcolor=bgcolor,
    )
    text = ft.Text("Hello, Flet!")
    textfield = ft.TextField(hint_text="enter text")

    def change(e):
        text.value = str(textfield.value)
        if text.value == "":
            pass
        else:
            page.update()

    page.add(
        ft.SafeArea(ft.Row(controls=[text, ft.IconButton(icon=ft.icons.PLAY_ARROW)]))
    )
    page.add(ft.SafeArea(ft.Row(controls=[textfield])))
    page.add(ft.SafeArea(ft.TextButton(text="Change Text", on_click=change)))
    page.add(ft.SafeArea(ft.ElevatedButton(text="Test", adaptive=True)))
    for i in btnlist:
        page.add(
            ft.SafeArea(
                ft.TextButton(f"test {i}"),
            )
        )


ft.app(target=main)
