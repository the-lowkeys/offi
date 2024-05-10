# This file

# Package Imports
import flet as ft
from flet import TextField, ElevatedButton, Checkbox, Text, Row, Column
from flet_core.control_event import ControlEvent


# Login Page Values

# Login Page Method Call
def draw(page, debug=False, handlers: dict=None):
    # Type Check
    if type(page) != ft.Page:
        raise TypeError('Argument \'page\' is not an \'flet.Page\' object!')
    
    # Draw Screen
    page.vertical_alignment = ft.MainAxisAlignment.CENTER
    page.horizontal_alignment = ft.CrossAxisAlignment.CENTER
    page.window_resizable = True
    txt = ft.Text(value="Welcome to OFFI", text_align=ft.TextAlign.CENTER, width=500, size=50)
    page.add(txt)
    
    text_username: TextField = TextField(label='Email', text_align=ft.TextAlign.LEFT, width=500)
    text_password: TextField = TextField(label='Password', text_align=ft.TextAlign.LEFT, width=500, password=True, can_reveal_password=True)
    button_submit: ElevatedButton = ElevatedButton(text='Login', width=200, height=75, disabled=True)
    
    def validate_username(e: ControlEvent) -> None:
        text_username.value = text_username.value.strip()
        if text_username.value.isascii():
            button_submit.disabled = True
            text_username.border_color = 'default'
            if all([text_username.value, text_password.value]):
                button_submit.disabled = False
        else:
            text_username.border_color = 'red'
        page.update()

    def validate_password(e: ControlEvent) -> None:
        text_password.value = text_password.value.strip()
        if text_password.value.isascii():          
            button_submit.disabled = True
            text_password.border_color = 'default'
            if all([text_username.value, text_password.value]):
                button_submit.disabled = False
        else:
            text_password.border_color = 'red'
        page.update()
        
    # Handler for Button Click
    def key_submit(e: ControlEvent):
        # Check if Employee Exists, if their passwords are correct, their role, 
        # Then sends the right screen to them.
        check = handlers['check-creds']({
            'user-email': text_username.value,
            'user-key': text_password.value
        })

        if check == False:
            text_username.border_color = 'red'
            text_password.border_color = 'red'
            page.update()
            return
        
        # Function Call Cascade
        handlers['set-user'](int(check[0]))
        if check[1] == 'EMPLOYEE': handlers['change-screen']('__REQUEST')
        elif check[1] == 'VALIDATOR': handlers['change-screen']('__VALIDATE')
        elif check[1] == 'KEEPER': handlers['change-screen']('__KEEPER')

    text_username.on_change = validate_username
    text_password.on_change = validate_password
    button_submit.on_click = key_submit
    
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
    

    