import flet as ft
from localisation import check_rtl, CONTNUEBTN, HELLOMSG
from infos import myappbar
from components import mybutton
import asyncio


def home(page, bgcolor, decoration):
    return ft.View(
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
                    rtl=check_rtl(page=page),
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
                                        on_click=lambda _: asyncio.create_task(
                                            page.push_route("/portfolio"),
                                        ),
                                    )
                                ],
                                alignment=ft.MainAxisAlignment.CENTER,
                            ),
                            alignment=ft.alignment.center,
                        ),
                    ],
                    expand=True,
                    alignment=ft.MainAxisAlignment.SPACE_EVENLY,
                )
            )
        ],
    )
