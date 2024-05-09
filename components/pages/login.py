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
    if type(handlers) != None:
        if type(handlers) != tuple:
            raise TypeError('Argument \'handlers\' is not of type \'tuple\'')
    
    # Draw Screen
    page.vertical_alignment = ft.MainAxisAlignment.CENTER
    
    text_username: TextField = TextField(label='Username', text_align=ft.TextAlign.LEFT, width=200)
    text_password: TextField = TextField(label='Password', text_align=ft.TextAlign.LEFT, width=200, password=True)
    checkbox_signup: Checkbox = Checkbox(label='i agree to this cresidentials', value=False)
    button_submit: ElevatedButton = ElevatedButton(text='submit', width=200, disabled=True)
    
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

    checkbox_signup.on_change = validate
    text_username.on_change = validate
    text_password.on_change = validate
    button_submit.on_click = submit
    
    page.add(
        Row(
            controls=[
                Column(
                    [text_username,
                     text_password,
                     checkbox_signup,
                     button_submit]
                )
            ],
            alignment=ft.MainAxisAlignment.CENTER
        )
    )
    


def get_info():
    pass
    