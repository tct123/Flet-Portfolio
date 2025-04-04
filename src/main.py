import flet as ft
from infos import myappbar
from background import mydecoration
from localisation import *
import flet_flashlight as ffl


def mybutton(text: str, on_click, disabled: bool = False):
    container = ft.ElevatedButton(
        content=ft.Text(text, size=20),
        height=50,
        on_click=on_click,
        bgcolor={
            ft.ControlState.DEFAULT: ft.Colors.RED,
            ft.ControlState.PRESSED: ft.Colors.TRANSPARENT,
        },
        expand=True,
        disabled=disabled,
    )

    return container


def is_mobile(platform: str):
    if platform in ["android", "ios"]:
        return False
    else:
        return True


def main(page: ft.Page):
    bgcolor = ft.Colors.TRANSPARENT
    page.title = "Flet Portfolio"
    flashlight = ffl.Flashlight()
    platform = page.platform.name.lower()
    page.window.min_height = 500
    page.window.min_width = 500
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
                                            disabled=False,
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
                                        text=FLASHLIGHTMSG(page=page),
                                        on_click=lambda _: page.go("/flashlight"),
                                        disabled=is_mobile(platform),
                                    ),
                                    mybutton(
                                        text="Zurück",
                                        on_click=lambda _: page.go("/"),
                                        disabled=False,
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
