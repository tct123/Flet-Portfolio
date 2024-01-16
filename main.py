import flet as ft


def main(page: ft.Page):
    page.title = "Portfolio"
    page.appbar = ft.AppBar(title=ft.Text(page.title))
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
    page.add(
        ft.SafeArea(
            ft.TextButton(text="Change Text", on_click=change)
        )
    )


ft.app(main)
