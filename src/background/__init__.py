import flet as ft


def mydecoration():
    return ft.BoxDecoration(
        image=ft.DecorationImage(
            src="images/picture1.jpg",
            fit=ft.BoxFit.COVER,
            opacity=0.2,
        ),
        gradient=ft.LinearGradient(
            colors=[ft.Colors.RED, ft.Colors.BLUE],
            stops=[0, 1],
            begin=ft.Alignment.TOP_LEFT,
            end=ft.Alignment.BOTTOM_RIGHT,
        ),
    )
