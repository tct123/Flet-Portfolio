import flet as ft
from localisation import check_rtl, CONTNUEBTN, HELLOMSG
from infos import myappbar
from components import mybutton
from localisation import HELLOMSG, CONTNUEBTN, FLASHLIGHTMSG


def flashlight(page, decoration, bgcolor):
    return ft.View(
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
                    rtl=check_rtl(page=page),
                    controls=[
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
                                    on_click=lambda _: print("Flashlight toggled"),
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
