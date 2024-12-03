import flet as ft


def openweb(e, page, url):
    page.launch_url(url=url)
    page.update()
