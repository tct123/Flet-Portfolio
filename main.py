import flet as ft
import colors as cs

bgcolor = cs.RED


def main(page: ft.Page):
    page.title = "Portfolio"
    page.bgcolor = bgcolor
    page.appbar = ft.AppBar(title=ft.Text(page.title), bgcolor=bgcolor)
    text = ft.Text("Hello, Flet!")
    textfield = ft.TextField(hint_text="enter text")

    def change(e):
        text.value = str(textfield.value)
        if text.value == "":
            pass
        else:
            page.update()

    page.add(
        ft.SafeArea(
            ft.Row(
                controls=[
                    text,
                ]
            )
        )
    )
    page.add(ft.SafeArea(ft.Row(controls=[textfield])))
    page.add(ft.SafeArea(ft.TextButton(text="Change Text", on_click=change)))
    page.add(ft.SafeArea(ft.Row(controls=[ft.TextButton(text="Github"),ft.TextButton(text="Github")])))


ft.app(main)
