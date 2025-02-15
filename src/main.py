import flet as ft
from infos import myappbar
from background import mydecoration


def main(page: ft.Page):
    bgcolor=ft.Colors.TRANSPARENT
    page.title = "Flet Portfolio"
    def route_change(e):
        page.views.clear()

        if page.route == "/":
            page.views.append(
                ft.View(
                    decoration=mydecoration(),
                    bgcolor=bgcolor,
                    route="/",
                    appbar=myappbar(page=page),
                    controls=[
                        ft.Text("Home Seite"),
                        ft.ElevatedButton(
                            "Gehe zu /about", on_click=lambda _: page.go("/about")
                        ),
                    ],
                )
            )
        elif page.route == "/about":
            page.views.append(
                ft.View(
                    decoration=mydecoration(),
                    bgcolor=bgcolor,
                    route="/about",
                    appbar=myappbar(page=page),
                    controls=[
                        ft.Text("Über uns"),
                        ft.ElevatedButton("Zurück", on_click=lambda _: page.go("/")),
                    ],
                )
            )

        page.update()

    page.on_route_change = route_change
    page.go(page.route)


ft.app(target=main)
