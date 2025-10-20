import flet as ft
from localisation import APPBARTOOLTIPMSG


def myappbar(page):
    bgcolor = ft.Colors.TRANSPARENT
    return ft.AppBar(
        title=ft.Text(page.title),
        center_title=True,
        adaptive=True,
        bgcolor=bgcolor,
        actions=[
            ft.PopupMenuButton(
                bgcolor=bgcolor,
                tooltip=APPBARTOOLTIPMSG(page=page),
                items=[
                    ft.PopupMenuItem(
                        icon=ft.Icons.CLOUD,
                        text="Github",
                        on_click=lambda _: page.launch_url(
                            url="https://github.com/tct123"
                        ),
                    ),
                    ft.PopupMenuItem(
                        icon=ft.Icons.PLAY_CIRCLE,
                        text="YouTube",
                        on_click=lambda _: page.launch_url(
                            url="https://youtube.com/@tc-diy"
                        ),
                    ),
                ],
            )
        ],
    )
