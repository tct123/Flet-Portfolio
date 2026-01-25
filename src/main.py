import flet as ft
from infos import myappbar
from background import mydecoration
from flet.app import os
from mylocale import TR
from flet_localisation import locale
from localisation.translations import check_rtl
from views import home, portfolio, flashlight
import asyncio

# import flet_flashlight as ffl
trfile = f"{os.path.dirname(__file__)}/localisation/localisation.csv"
print(trfile)


async def main(page: ft.Page):
    def on_resized(e):
        print(f"Fenstergröße geändert: {page.window.width}x{page.window.height}")
        page.update()

    page.adaptive = True
    page.title = "Flet Portfolio"
    page.window.min_height = 500
    page.window.min_width = 500
    page.on_resized = on_resized

    # Standard-Dekoration
    bgcolor = ft.Colors.TRANSPARENT
    decoration = mydecoration()

    def route_change(e):
        page.views.clear()
        if page.route == "/":
            page.views.append(home(page=page, bgcolor=bgcolor, decoration=decoration))
        elif page.route == "/portfolio":
            page.views.append(
                portfolio(page=page, decoration=decoration, bgcolor=bgcolor)
            )
        elif page.route == "/flashlight":
            page.views.append(
                flashlight(page=page, decoration=decoration, bgcolor=bgcolor)
            )
        page.update()

    page.on_route_change = route_change
    await asyncio.create_task(page.push_route(page.route))


ft.run(main=main)
