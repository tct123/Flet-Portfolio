import flet as ft
import colors as cs
import openweb as ob

bgcolor = cs.RED


def main(page: ft.Page):
    page.title = "Portfolio"
    # page.bgcolor = bgcolor
    def opengithub(e):
        ob.openweb(e=e, page=page, url="https://github.com/tct123")
    def openyt1(e):
        ob.openweb(e=e, page=page, url="https://youtube.com/@tc-diy")

    page.appbar = ft.AppBar(
        title=ft.Text(page.title),
        bgcolor=bgcolor,
        actions=[
            ft.PopupMenuButton(
                items=[
                    ft.PopupMenuItem(icon=ft.icons.CLOUD,text="Github", on_click=opengithub),
                    ft.PopupMenuItem(icon=ft.icons.PLAY_CIRCLE,text="YouTube", on_click=openyt1),
                ]
            )
        ],
    )
    page.bottom_appbar = ft.BottomAppBar(
        content=ft.Row(
            controls=[
                ft.IconButton(icon=ft.icons.MENU, icon_color=ft.colors.WHITE),
                ft.Container(expand=True),
            ]
        ),
        bgcolor=bgcolor,
    )
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


ft.app(main)
