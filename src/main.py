import flet as ft
from infos import myappbar
from background import mydecoration


def mybutton(text, width, on_click):
    return ft.Container(
        content=ft.Text(text, size=20),
        height=50,
        width=width,
        on_click=on_click,
        bgcolor=ft.Colors.RED,
        border_radius=10,
        alignment=ft.alignment.center,
    )


def main(page: ft.Page):
    bgcolor = ft.Colors.TRANSPARENT
    page.title = "Flet Portfolio"

    def route_change(e):
        page.views.clear()

        if page.route == "/":
            page.views.append(
                ft.View(
                    horizontal_alignment=ft.CrossAxisAlignment.CENTER,
                    vertical_alignment=ft.MainAxisAlignment.CENTER,
                    decoration=mydecoration(),
                    bgcolor=bgcolor,
                    route="/",
                    appbar=myappbar(page=page),
                    controls=[
                        ft.SafeArea(
                            ft.Column(
                                horizontal_alignment=ft.CrossAxisAlignment.CENTER,
                                controls=[
                                    ft.Column(
                                        controls=[
                                            ft.Text(
                                                "Hello. This is my Portfolio", size=100
                                            )
                                        ]
                                    ),
                                    ft.Column(
                                        controls=[
                                            mybutton(
                                                text="Continue",
                                                on_click=lambda _: page.go("/about"),
                                                width=page.width,
                                            )
                                        ],
                                    ),
                                ],
                            )
                        )
                    ],
                )
            )
        elif page.route == "/about":
            page.views.append(
                ft.View(
                    horizontal_alignment=ft.CrossAxisAlignment.CENTER,
                    vertical_alignment=ft.MainAxisAlignment.CENTER,
                    decoration=mydecoration(),
                    bgcolor=bgcolor,
                    route="/about",
                    appbar=myappbar(page=page),
                    controls=[
                        ft.SafeArea(
                            ft.Column(
                                [
                                    ft.Text("Über uns"),
                                    mybutton(
                                        text="Zurück",
                                        on_click=lambda _: page.go("/"),
                                        width=page.width,
                                    ),
                                ]
                            )
                        )
                    ],
                )
            )

        page.update()

    page.on_route_change = route_change
    page.go(page.route)


ft.app(target=main)
