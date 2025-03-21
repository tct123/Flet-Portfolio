import flet as ft


def main(page: ft.Page):
    colors = page.client_storage.get("favorite_colors")
    def handle_nav_change(e):
        page.controls.clear()
        selected_index = page.navigation_bar.selected_index if e is None else e.control.selected_index
        if selected_index == 0:
            page.add(ft.Text("Explore!"))
        elif selected_index == 1:
            page.add(ft.Text("Commute!"))
        elif selected_index == 2:
            page.add(ft.Text("Bookmark!"))
        page.update()
    def set_selected_index():
        page.navigation_bar.selected_index = 0
        handle_nav_change(None)
    page.title = "NavigationBar Example"
    page.navigation_bar = ft.NavigationBar(
        on_change=handle_nav_change,
        destinations=[
            ft.NavigationBarDestination(icon=ft.Icons.EXPLORE, label="Explore"),
            ft.NavigationBarDestination(icon=ft.Icons.COMMUTE, label="Commute"),
            ft.NavigationBarDestination(
                icon=ft.Icons.BOOKMARK_BORDER,
                selected_icon=ft.Icons.BOOKMARK,
                label="Bookmark",
            ),
        ],
    )
    page.add(ft.Text("Hello"))
    set_selected_index()
ft.app(target=main)
