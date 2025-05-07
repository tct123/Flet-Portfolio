import flet as ft
from infos import myappbar
from background import mydecoration
from localisation import HELLOMSG, CONTNUEBTN, FLASHLIGHTMSG

# import flet_flashlight as ffl


def mybutton(page, text: str, on_click, disabled: bool = False):
    return ft.ElevatedButton(
        adaptive=True,
        content=ft.Text(text, size=20),
        height=50,
        expand=True,  # Automatische Anpassung der Breite
        on_click=on_click,
        bgcolor={
            ft.ControlState.DEFAULT: ft.Colors.RED,
            ft.ControlState.PRESSED: ft.Colors.TRANSPARENT,
        },
        disabled=disabled,
        style=ft.ButtonStyle(shape=ft.RoundedRectangleBorder(radius=10)),
    )


def main(page: ft.Page):
    def on_resized(e):
        print(f"Fenstergröße geändert: {page.window.width}x{page.window.height}")
        page.update()

    page.adaptive = True
    page.title = "Flet Portfolio"
    page.window.min_height = 500
    page.window.min_width = 500
    page.on_resized = on_resized

    # Standard-Dekoration
    bgcolor = ft.Colors.TRANSPARENT
    decoration = mydecoration()

    def route_change(e):
        page.views.clear()
        if page.route == "/":
            page.views.append(
                ft.View(
                    adaptive=True,
                    scroll=True,
                    horizontal_alignment=ft.CrossAxisAlignment.CENTER,
                    vertical_alignment=ft.MainAxisAlignment.CENTER,
                    decoration=decoration,  # Dekoration angewendet
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
                                            HELLOMSG(page=page),  # Lokalisierter Text
                                            size=100,
                                            text_align=ft.TextAlign.CENTER,
                                        ),
                                    ),
                                    ft.Container(
                                        content=ft.Row(
                                            [
                                                mybutton(
                                                    page=page,
                                                    text=CONTNUEBTN(
                                                        page=page
                                                    ),  # Lokalisierter Text
                                                    on_click=lambda _: page.go(
                                                        "/portfolio"
                                                    ),
                                                )
                                            ],
                                            alignment=ft.MainAxisAlignment.CENTER,
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
                    adaptive=True,
                    horizontal_alignment=ft.CrossAxisAlignment.CENTER,
                    vertical_alignment=ft.MainAxisAlignment.CENTER,
                    decoration=decoration,  # Dekoration angewendet
                    bgcolor=bgcolor,
                    route="/portfolio",
                    appbar=myappbar(page=page),
                    controls=[
                        ft.SafeArea(
                            ft.Column(
                                [
                                    ft.Row(
                                        [ft.Text("Portfolio")],
                                        alignment=ft.MainAxisAlignment.CENTER,
                                    ),
                                    ft.Row(
                                        [
                                            mybutton(
                                                page=page,
                                                text=FLASHLIGHTMSG(
                                                    page=page
                                                ),  # Lokalisierter Text
                                                on_click=lambda _: page.go(
                                                    "/flashlight"
                                                ),
                                            )
                                        ],
                                        alignment=ft.MainAxisAlignment.CENTER,
                                    ),
                                    ft.Row(
                                        [
                                            mybutton(
                                                page=page,
                                                text="Zurück",
                                                on_click=lambda _: page.go("/"),
                                            )
                                        ],
                                        alignment=ft.MainAxisAlignment.CENTER,
                                    ),
                                ],
                                expand=True,
                            )
                        )
                    ],
                )
            )
        elif page.route == "/flashlight":
            page.views.append(
                ft.View(
                    adaptive=True,
                    horizontal_alignment=ft.CrossAxisAlignment.CENTER,
                    vertical_alignment=ft.MainAxisAlignment.CENTER,
                    decoration=decoration,  # Dekoration angewendet
                    bgcolor=bgcolor,
                    route="/flashlight",
                    appbar=myappbar(page=page),
                    controls=[
                        ft.SafeArea(
                            ft.Column(
                                [
                                    ft.Row(
                                        [ft.Text("Über uns")],
                                        alignment=ft.MainAxisAlignment.CENTER,
                                    ),
                                    ft.Row(
                                        [
                                            ft.TextButton(
                                                text="On/Off",
                                                disabled=True,
                                                icon=ft.Icons.FLASH_AUTO,
                                                on_click=lambda _: print(
                                                    "Flashlight toggled"
                                                ),
                                            )
                                        ],
                                        alignment=ft.MainAxisAlignment.CENTER,
                                    ),
                                    ft.Row(
                                        [
                                            mybutton(
                                                page=page,
                                                text="Zurück",
                                                on_click=lambda _: page.go("/"),
                                            )
                                        ],
                                        alignment=ft.MainAxisAlignment.CENTER,
                                    ),
                                ],
                                expand=True,
                            )
                        )
                    ],
                )
            )
        page.update()

    page.on_route_change = route_change
    page.go(page.route)


ft.app(target=main)
