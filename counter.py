import flet as ft
import time

def main(page: ft.Page):

    # Set the page title
    page.title = "Counter with Flet"

    # Create a text widget (centered)
    text1 = ft.Text(value="Count down..!", size=60, color="blue")
    row1 = ft.Row(controls=[text1], alignment="center")  # Proper enum
    page.add(row1)

    # Create another text widget for the countdown (centered)
    text2 = ft.Text(size=40, color="red")
    row2 = ft.Row(controls=[text2], alignment="center")  # Shorthand string
    page.add(row2)
    for i in range(10, -1, -1):
        text2.value = i
        page.update()
        time.sleep(1)



# Run the Flet app
ft.app(target=main)