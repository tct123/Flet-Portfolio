import flet as ft


def main(page: ft.Page):
    colors = page.client_storage.get("favorite_colors")
    print(colors)

    def handle_nav_change(e):
        # Clear the current controls and add the new controls based on the selected index
        page.controls.clear()
        if e.control.selected_index == 0:
            page.add(ft.Text("Explore!"))
        elif e.control.selected_index == 1:
            page.add(ft.Text("Commute!"))
        elif e.control.selected_index == 2:
            page.add(ft.Text("Bookmark!"))
        page.update()

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
    # Add an initial control
    page.add(ft.Text(f"{colors}"))


ft.app(target=main)
