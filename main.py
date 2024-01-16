import flet as ft


def main(page: ft.Page):
    page.title = "Portfolio"
    page.appbar = ft.AppBar(title=ft.Text(page.title))
    text = ft.Text("Hello, Flet!")
    textfield = ft.TextField()
    def change(e):
        text.value = str(textfield.value)
        page.update()
    page.add(
        ft.SafeArea(
            ft.Row(
                controls=[
                    text,
                    ft.TextButton(text="Change Text", on_click=change)
                ]
            ),
            ft.Row(controls=[ft.Text("Next")])
        )
    )
    page.add(ft.SafeArea(ft.Row(controls=[textfield])))

    


ft.app(main)
