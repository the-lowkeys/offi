# This file

# Package Imports
import flet as ft
from flet import TextField, ElevatedButton, Checkbox, Text, Row, Column
from flet_core.control_event import ControlEvent


# Login Page Values

# Login Page Method Call
def draw(page, debug=False, handlers: tuple=None):
    # Type Check
    if type(page) != ft.Page:
        raise TypeError('Argument \'page\' is not an \'flet.Page\' object!')
    
    # Draw Screen
    page.vertical_alignment = ft.MainAxisAlignment.CENTER
    page.horizontal_alignment = ft.CrossAxisAlignment.CENTER
    page.window_resizable = True
    txt = ft.Text(value="Welcome to OFFI", text_align=ft.TextAlign.CENTER, width=500, size=50)
    page.add(txt)
    
    text_username: TextField = TextField(label='Employee ID', text_align=ft.TextAlign.LEFT, width=500)
    text_password: TextField = TextField(label='Password', text_align=ft.TextAlign.LEFT, width=500, password=True)
    button_submit: ElevatedButton = ElevatedButton(text='Login', width=200, height=75, disabled=True)
    checkbox_show_password: Checkbox = Checkbox(label='Show Password', value=False)
    
    def validate(e:ControlEvent) ->None:
        if text_username.value.isdigit() and len(text_username.value) <= 10:
            if all([text_username.value, text_password.value]):
                button_submit.disabled = False
            else:
                button_submit.disabled = True
        else:
            text_username.value = ''
            text_username.border_color = 'red'
            print('Invalid input. Please enter up to 10 digits.')
        page.update()
        
    def toggle_password_visibility(e:ControlEvent) -> None:
        text_password.password = not checkbox_show_password.value
        page.update()

    def submit(e:ControlEvent) -> None:
        print('Username:', text_username.value)
        print('Password:', text_password.value)
        

    text_username.on_change = validate
    text_password.on_change = validate
    checkbox_show_password.on_change = toggle_password_visibility
    #button_submit.on_click = submit
    
    page.add(
        Row(
            controls=[text_username],
            alignment=ft.MainAxisAlignment.CENTER
        )
    )
    page.add(
        Row(
            controls=[text_password],
            alignment=ft.MainAxisAlignment.CENTER
        )
    )
    page.add(
        Row(
            controls=[checkbox_show_password],
            alignment=ft.MainAxisAlignment.CENTER
        )
    )

    page.add(
        Row(
            controls=[button_submit],
            alignment=ft.MainAxisAlignment.CENTER
        )
    )
    


def get_info():
    pass
    