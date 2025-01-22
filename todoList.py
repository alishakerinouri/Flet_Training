import flet as ft

def main(page: ft.Page):
    
    def add_task(e):
        check_box = ft.Checkbox(label= text_task.value)
        page.add(check_box)
        text_task.value = ""
        page.update()         
    
    page.title = "ToDo List"

    Welcome_text = ft.Text(value="Welcome to ToDo List!", size=60, color="blue")
    row2 = ft.Row(controls=[Welcome_text],alignment="center")
    page.add(row2)

    text_task = ft.TextField(label="Enter the task : ", width=300)
    task_button = ft.ElevatedButton(text= "Add", on_click= add_task)
    row1 = ft.Row(controls=[text_task,task_button], alignment="center")
    page.add(row1)

    # Run the Flet app
ft.app(target=main)

