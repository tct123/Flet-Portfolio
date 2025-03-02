import os
from mylocale import tr
from flet_localisation import locale
import flet as ft

trfile = f"{os.path.dirname(__file__)}/localisation.csv"
HELLOMSG = tr(
    csv_file=trfile,
    target_key="HELLOMSG",
    langcode=locale(str(ft.Page.platform)),
)
