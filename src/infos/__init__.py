import flet as ft
from localisation import APPBARTOOLTIPMSG
import asyncio


async def myappbar(page):
    bgcolor = ft.Colors.TRANSPARENT
    url_launcher = ft.UrlLauncher()

    async def launch_default(e: ft.Event[ft.PopupMenuItem]):
        url = e.control.data
        print(url)
        await url_launcher.launch_url(url=url)

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
                        content=ft.Text("Github"),
                        on_click=launch_default,
                        data="https://github.com/tct123",
                    ),
                    ft.PopupMenuItem(
                        icon=ft.Icons.PLAY_CIRCLE,
                        content=ft.Text("YouTube"),
                        on_click=launch_default,
                        data="https://youtube.com/@tc-diy",
                    ),
                ],
            )
        ],
    )
