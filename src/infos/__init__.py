import flet as ft


def myappbar(page):
    return ft.AppBar(
        title=ft.Text(page.title),
        center_title=True,
        adaptive=True,
        bgcolor=page.bgcolor,
        actions=[
            ft.PopupMenuButton(
                bgcolor=page.bgcolor,
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
