import os
import platform
from mylocale import tr
from flet_localisation import locale
import flet as ft

myplatfom = platform.system().lower()
trfile = f"{os.path.dirname(__file__)}/localisation.csv"
langcode=locale(platform=myplatfom).split("_")[0]
print(langcode)
HELLOMSG = tr(
    csv_file=trfile,
    target_key="HELLOMSG",
    langcode=langcode,
)
