import flet as ft
import colors as cs
import os
from infos import myappbar
from background import mydecoration


def mycontainer(text, width, on_click):  # page.width
    return ft.Container(
        ft.Text(text),
        bgcolor=ft.Colors.WHITE,
        width=width,
        height=50,
        border_radius=10,
        on_click=on_click,
    )


def main(page: ft.Page):
    page.go("/")
    page.title = "Flet Portfolio"
    bgcolor = ft.Colors.TRANSPARENT
    page.vertical_alignment = ft.MainAxisAlignment.CENTER
    page.horizontal_alignment = ft.CrossAxisAlignment.CENTER
    page.scroll = True

    def route_change(e: ft.RouteChangeEvent):
        page.views.clear()
        page.views.append(
            ft.View(
                route="/",
                appbar=myappbar(
                    title="Flet Portfolio",
                    bgcolor=bgcolor,
                    items=[
                        ft.PopupMenuItem(
                            icon=ft.Icons.CLOUD,
                            text="GitHub",
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
                ),
                decoration=mydecoration(),
                controls=[
                    ft.Column(
                        controls=[
                            mycontainer(
                                text="Simple hello World",
                                width=page.width,
                                on_click=lambda _: page.go("/hello"),
                            )
                        ]
                    )
                ],
                vertical_alignment=ft.MainAxisAlignment.CENTER,
                horizontal_alignment=ft.CrossAxisAlignment.CENTER,
            )
        )
        if page.route == "/hello":
            page.views.append(
                ft.View(
                    route="/hello",
                    appbar=myappbar(page=page),
                    controls=[ft.Column(controls=[ft.Text("Hello")])],
                    vertical_alignment=ft.MainAxisAlignment.CENTER,
                    horizontal_alignment=ft.CrossAxisAlignment.CENTER,
                )
            )

    page.on_route_change = route_change
    page.go(page.route)


ft.app(target=main)
