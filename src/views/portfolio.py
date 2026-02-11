import flet as ft
from localisation import check_rtl, CONTNUEBTN, HELLOMSG
from infos import myappbar
from components import mybutton
from localisation import HELLOMSG, CONTNUEBTN, FLASHLIGHTMSG
import asyncio


async def portfolio(page: ft.Page, decoration, bgcolor):
    return ft.View(
        horizontal_alignment=ft.CrossAxisAlignment.CENTER,
        vertical_alignment=ft.MainAxisAlignment.CENTER,
        decoration=decoration,  # Dekoration angewendet
        bgcolor=bgcolor,
        route="/portfolio",
        appbar=await myappbar(page=page),
        controls=[
            ft.SafeArea(
                ft.Column(
                    rtl=check_rtl(page=page),
                    controls=[
                        ft.Row(
                            [ft.Text("Portfolio")],
                            alignment=ft.MainAxisAlignment.CENTER,
                        ),
                        ft.Row(
                            [
                                mybutton(
                                    page=page,
                                    text=FLASHLIGHTMSG(page=page),  # Lokalisierter Text
                                    on_click=lambda _: asyncio.create_task(
                                        page.push_route("/flashlight"),
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
                                    on_click=lambda _: asyncio.create_task(
                                        page.push_route("/"),
                                    ),
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
