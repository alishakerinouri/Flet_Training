import flet as ft

def main(page: ft.Page):
    def login_to(e):
        TextLogin = ft.Text(value="Hello "+textbox.value, size=30, color="green")
        row4 = ft.Row(controls=[TextLogin], alignment="center")
        page.add(row4)
    # Set the page title
    page.title = "Login page"

    # Add text box and button
    textbox = ft.TextField(label="Enter your name : ")
    login_button = ft.ElevatedButton(text="Login",on_click= login_to)
    row3 = ft.Row(controls=[textbox,login_button], alignment="center")
    page.add(row3)

    # Run the Flet app
ft.app(target=main)