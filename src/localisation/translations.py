import os
from mylocale import TR
from flet_localisation import locale
import flet as ft

trfile = f"{os.path.dirname(__file__)}/localisation.csv"


def check_rtl(page):
    myplatfom = str(page.platform)
    langcode = str(locale(platform=myplatfom)).split("_")[0]
    region = str(locale(platform=myplatfom)).split("_")[1]
    tr = TR(langcode=langcode, csv_file=trfile)
    return tr.check_rtl(langcode=langcode)


def HELLOMSG(page):
    myplatfom = str(page.platform)
    langcode = str(locale(platform=myplatfom)).split("_")[0]
    region = str(locale(platform=myplatfom)).split("_")[1]
    tr = TR(langcode=langcode, csv_file=trfile)
    return tr.tr(
        target_key="HELLOMSG",
        langcode=langcode,
    )


def CONTNUEBTN(page):
    myplatfom = str(page.platform)
    langcode = str(locale(platform=myplatfom)).split("_")[0]
    region = str(locale(platform=myplatfom)).split("_")[1]
    tr = TR(langcode=langcode, csv_file=trfile)
    return tr.tr(
        target_key="CONTNUEBTN",
        langcode=langcode,
    )


def FLASHLIGHTMSG(page):
    myplatfom = str(page.platform)
    langcode = str(locale(platform=myplatfom)).split("_")[0]
    region = str(locale(platform=myplatfom)).split("_")[1]
    tr = TR(langcode=langcode, csv_file=trfile)
    return tr.tr(
        target_key="FLASHLIGHTMSG",
        langcode=langcode,
    )


def APPBARTOOLTIPMSG(page):
    myplatfom = str(page.platform)
    langcode = str(locale(platform=myplatfom)).split("_")[0]
    region = str(locale(platform=myplatfom)).split("_")[1]
    tr = TR(langcode=langcode, csv_file=trfile)
    return tr.tr(
        target_key="APPBARTOOLTIP",
        langcode=langcode,
    )
