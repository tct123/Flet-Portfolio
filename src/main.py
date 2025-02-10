import flet as ft
import colors as cs
import openweb as ob
import os
import flet_audio as fta

btnlist = ["1", "2"]


def main(page: ft.Page):
    bgcolor = ft.Colors.TRANSPARENT
    global playing
    playing = False
    page.title = "Portfolio"
    page.decoration = ft.BoxDecoration(
        image=ft.DecorationImage(
            src="images/picture1.jpg",
            fit=ft.ImageFit.COVER,
            opacity=0.2,
        ),
        gradient=ft.LinearGradient(
            colors=[ft.Colors.RED, ft.Colors.BLUE],
            stops=[0, 1],
            begin=ft.alignment.top_left,
            end=ft.alignment.bottom_right,
        ),
    )
    page.adaptive = True
    page.bgcolor = bgcolor
    music = fta.Audio(src="mozart.mp3")
    page.overlay.append(music)
    page.scroll = True

    def opengithub(e):
        ob.openweb(e=e, page=page, url="https://github.com/tct123")

    def openyt1(e):
        ob.openweb(e=e, page=page, url="https://youtube.com/@tc-diy")

    page.appbar = ft.AppBar(
        title=ft.Text(page.title),
        center_title=True,
        adaptive=True,
        bgcolor=bgcolor,
        actions=[
            ft.PopupMenuButton(
                items=[
                    ft.PopupMenuItem(
                        icon=ft.Icons.CLOUD, text="Github", on_click=opengithub
                    ),
                    ft.PopupMenuItem(
                        icon=ft.Icons.PLAY_CIRCLE, text="YouTube", on_click=openyt1
                    ),
                ]
            )
        ],
    )
    page.bottom_appbar = ft.BottomAppBar(
        bgcolor=bgcolor,
        content=ft.Row(
            controls=[
                ft.IconButton(icon=ft.Icons.MENU, icon_color=ft.Colors.WHITE),
                ft.Container(expand=True),
            ]
        ),
    )
    text = ft.Text("Hello, Flet!")
    textfield = ft.TextField(hint_text="enter text")

    def change(e):
        text.value = str(textfield.value)
        if text.value == "":
            pass
        else:
            page.update()

    def play(e):
        global playing
        if playing == False:
            music.play()
            playing = True
        else:
            music.pause()
            playing = False

    page.add(
        ft.SafeArea(
            ft.Row(
                controls=[text, ft.IconButton(icon=ft.Icons.PLAY_ARROW, on_click=play)]
            )
        )
    )
    page.add(
        ft.SafeArea(
            ft.Row(
                controls=[
                    textfield,
                    ft.TextButton(text="Change Text", on_click=change),
                    ft.ElevatedButton(text="Test", adaptive=True),
                ]
            )
        )
    )
    for i in btnlist:
        page.add(
            ft.SafeArea(
                ft.TextButton(f"test {i}"),
            )
        )


ft.app(target=main)
