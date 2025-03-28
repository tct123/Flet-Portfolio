import flet as ft
from infos import myappbar
from background import mydecoration
from localisation import *
import flet_flashlight as ffl


def mybutton(text, on_click):
    def hover(e):
        if e.data == "true":
            e.control.opacity = 0.5
            e.control.update()
        else:
            e.control.opacity = 1
            e.control.update()

    container = ft.Container(
        content=ft.Text(text, size=20),
        height=50,
        on_click=on_click,
        bgcolor=ft.Colors.RED,
        border_radius=10,
        alignment=ft.alignment.center,
        expand=True,
        on_hover=hover,
    )

    return container


def main(page: ft.Page):
    bgcolor = ft.Colors.TRANSPARENT
    page.title = "Flet Portfolio"
    flashlight = ffl.Flashlight()
    platform = page.platform.name.lower()
    page.window.min_height = 500
    page.window.min_width = 500
    print(platform)
    if platform in ["android", "ios"]:
        page.overlay.append(flashlight)

    def route_change(e):
        page.views.clear()
        if page.route == "/":
            page.views.append(
                ft.View(
                    scroll=True,
                    horizontal_alignment=ft.CrossAxisAlignment.CENTER,
                    vertical_alignment=ft.MainAxisAlignment.CENTER,
                    decoration=mydecoration(),
                    bgcolor=bgcolor,
                    route="/",
                    appbar=myappbar(page=page),
                    controls=[
                        ft.SafeArea(
                            ft.Column(
                                controls=[
                                    ft.Container(
                                        alignment=ft.alignment.center,
                                        content=ft.Text(
                                            HELLOMSG(page=page),
                                            size=100,
                                            text_align=ft.TextAlign.CENTER,
                                        ),
                                    ),
                                    ft.Container(
                                        content=mybutton(
                                            text=CONTNUEBTN(page=page),
                                            on_click=lambda _: page.go("/portfolio"),
                                        ),
                                        alignment=ft.alignment.center,
                                    ),
                                ],
                                expand=True,
                            )
                        )
                    ],
                )
            )
        elif page.route == "/portfolio":
            page.views.append(
                ft.View(
                    horizontal_alignment=ft.CrossAxisAlignment.CENTER,
                    vertical_alignment=ft.MainAxisAlignment.CENTER,
                    decoration=mydecoration(),
                    bgcolor=bgcolor,
                    route="/portfolio",
                    appbar=myappbar(page=page),
                    controls=[
                        ft.SafeArea(
                            ft.Column(
                                [
                                    ft.Text("Portfolio"),
                                    mybutton(
                                        text="flashlight",
                                        on_click=lambda _: page.go("/flashlight"),
                                    ),
                                    mybutton(
                                        text="Zurück",
                                        on_click=lambda _: page.go("/"),
                                    ),
                                ],
                            )
                        )
                    ],
                )
            )
        elif page.route == "/flashlight":
            page.views.append(
                ft.View(
                    horizontal_alignment=ft.CrossAxisAlignment.CENTER,
                    vertical_alignment=ft.MainAxisAlignment.CENTER,
                    decoration=mydecoration(),
                    bgcolor=bgcolor,
                    route="/flashlight",
                    appbar=myappbar(page=page),
                    controls=[
                        ft.SafeArea(
                            ft.Column(
                                [
                                    ft.Text("Über uns"),
                                    ft.TextButton(
                                        text="On/Off",
                                        icon=ft.Icons.FLASH_AUTO,
                                        on_click=lambda _: flashlight.toggle(),
                                    ),
                                    mybutton(
                                        text="Zurück",
                                        on_click=lambda _: page.go("/"),
                                    ),
                                ],
                            )
                        )
                    ],
                )
            )

        page.update()

    page.on_route_change = route_change
    page.go(page.route)


ft.app(target=main)
