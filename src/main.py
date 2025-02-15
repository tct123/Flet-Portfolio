import flet as ft
import colors as cs
import os
from background import mydecoration

def myappbar(title, bgcolor, items: list):
    return ft.AppBar(
        title=ft.Text(title),
        center_title=True,
        adaptive=True,
        bgcolor=bgcolor,
        actions=[
            ft.PopupMenuButton(
                bgcolor=bgcolor,
                items=items,
            )
        ],
    )
def mydecoration():
    return ft.BoxDecoration(
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

def mycontainer(text, width, on_click):  # page.width
    return ft.Container(
        ft.Text(text),
        bgcolor=ft.Colors.WHITE,
        width=width,
        height=50,
        border_radius=10,
        on_click=on_click,
    )


def main(page:ft.Page):
    page.title = "Flet Portfolio"


ft.app(target=main)
