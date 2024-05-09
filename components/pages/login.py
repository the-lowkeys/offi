# This file

# Package Imports
import flet as ft
from flet import TextField, ElevatedButton, Checkbox, Text, Row, Column
from flet_core.control_event import ControlEvent


# Login Page Values

# Login Page Method Call
def draw(page, debug=False):
    # Type Check
    if type(page) != ft.Page:
        raise TypeError('Argument \'page\' is not an \'flet.Page\' object!')
    
    # Draw Screen
    page.title = 'OFFI'
    page.vertical_alignment = ft.MainAxisAlignment.CENTER
    page.horizontal_alignment = ft.CrossAxisAlignment.CENTER
    page.theme_mode = ft.ThemeMode.DARK
    page.window_width = 700
    page.window_height = 700    
    page.window_resizable = True
    txt = ft.Text(value="Welcome to OFFI", text_align=ft.TextAlign.CENTER, width=500, size=50)
    page.add(txt)
    
    text_username: TextField = TextField(label='Username', text_align=ft.TextAlign.LEFT, width=500)
    text_password: TextField = TextField(label='Password', text_align=ft.TextAlign.LEFT, width=500, password=True)
    button_submit: ElevatedButton = ElevatedButton(text='Login', width=200, height=75, disabled=True)
    
    def validate(e:ControlEvent) ->None:
        if all([text_username.value, text_password.value]):
            button_submit.disabled = False
        else:
            button_submit.disabled = True
            
        page.update()
        
    def submit(e:ControlEvent) -> None:
        print('Username:', text_username.value)
        print('Password:', text_password.value)
        
        page.clean()
        page.add(
            Row(
                controls=[Text(value=f'Welcome: {text_username.value}', size=20)],
                alignment=ft.MainAxisAlignment.CENTER
            )
        )

    text_username.on_change = validate
    text_password.on_change = validate
    button_submit.on_click = submit
    
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
            controls=[button_submit],
            alignment=ft.MainAxisAlignment.CENTER
        )
    )

    


def get_info():
    pass
    