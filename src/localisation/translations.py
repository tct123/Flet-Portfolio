import os
import platform
from mylocale import tr
from flet_localisation import locale

myplatfom = platform.system().lower()
trfile = f"{os.path.dirname(__file__)}/localisation.csv"
langcode = locale(platform=myplatfom).split("_")[0]
region = locale(platform=myplatfom).split("_")[1]

HELLOMSG = tr(
    csv_file=trfile,
    target_key="HELLOMSG",
    langcode=langcode,
)
CONTNUEBTN = tr(
    csv_file=trfile,
    target_key="CONTNUEBTN",
    langcode=langcode,
)
