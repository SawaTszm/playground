# https://flet.dev/docs/
import flet as ft
import time


def main(page: ft.Page):
    t = ft.Text(value="Hello, world!", color="green")
    page.controls.append(t)
    page.update()

    t = ft.Text()
    page.add(t)  # it's a shortcut for page.controls.append(t) and then page.update()

    for i in range(3):
        t.value = f"Step {i}"
        page.update()
        time.sleep(1)

    page.add(
        ft.Row(controls=[
            ft.Text("A"),
            ft.Text("B"),
            ft.Text("C")
        ])
    )

    page.add(
        ft.Row(controls=[
            ft.TextField(label="Your name"),
            ft.ElevatedButton(text="Say my name!")
        ])
    )

    for i in range(10):
        page.controls.append(ft.Text(f"Line {i}"))
        if i > 4:
            page.controls.pop(0)
        page.update()
        time.sleep(0.3)

    def button_clicked(e):
        page.add(ft.Text("Clicked!"))

    page.add(ft.ElevatedButton(text="Click me", on_click=button_clicked))


ft.app(port=8550, target=main)
