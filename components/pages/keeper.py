# Package Imports
import flet as ft
from time import sleep

# Project Module Imports

# Requestor Page Method Call
def draw(page, debug=False, handlers: dict=None):
    # Type Check
    if type(page) != ft.Page:
        raise TypeError('Argument \'page\' is not an \'flet.Page\' object!')
        
    # Functions
    def selective_enable(e):
        pass

    def unfocus_strip(e):
        page_grid[1].controls[1].value = page_grid[1].controls[1].value.strip()
        page.update()
    
    def radio_select(e):
        pass

    def __return(e):
        handlers['change-screen']('__LOGIN')
    
    
    # Draw Screen
    page_grid = [
        ft.Row(
            [
                ft.Text('Administrator', 
                        text_align=ft.TextAlign.CENTER, 
                        size=36)
            ],
            spacing=0,
            wrap=False,
            alignment=ft.MainAxisAlignment.CENTER,
            vertical_alignment=ft.CrossAxisAlignment.START,
            height=50
        ),
        ft.Row(
            [
                ft.ElevatedButton(
                    content=ft.Container(
                        content=ft.Column(
                            [
                            ft.Text(value="Validate",
                                    size=13,
                                    ),
                            ],
                            alignment=ft.MainAxisAlignment.CENTER
                        )
                    )
                ),
                ft.ElevatedButton(
                        content=ft.Container(
                        content=ft.Column(
                            [
                            ft.Text(value="Cancel", 
                                    size=13,
                                    ),
                            ],
                            alignment=ft.MainAxisAlignment.CENTER
                        ),
                    )
                ),
                ft.ElevatedButton(
                        content=ft.Container(
                        content=ft.Column(
                            [
                            ft.Text(value="Return", 
                                    size=13,
                                    color='red'
                                    ),
                                    
                            ],
                            alignment=ft.MainAxisAlignment.CENTER,
                        ),
                        on_click=__return
                    )
                ),
                ft.TextField(
                    label='File Type',
                    width=300,
                    height=50,
                    multiline=True,
                    min_lines=6,
                    max_lines=6
                ),
                
            ],
            spacing=17,
            wrap=False,
            alignment=ft.MainAxisAlignment.CENTER,
            vertical_alignment=ft.CrossAxisAlignment.CENTER
        ),
        ft.Row(
            [
                ft.Row(
                    [
                        ft.Column([
                            ft.TextField(
                            label='File ID',
                            disabled=True    
                        ),
                            ft.TextField(
                            label='Cabinet ID',
                            disabled=True,
                            height=75    
                        ),
                            ft.TextField(
                            label='Data',
                            width=300,
                            height=150,
                            min_lines=4,
                            max_lines=4,
                            disabled=True
                        ),
                        ]),
                        
                        ft.Column(
                            [
                                ft.TextField(
                                    label='Drawer ID',
                                    multiline=True,
                                    disabled=True
                                ),
                                ft.TextField(
                                    label='Comment',
                                    multiline=True,
                                    min_lines=7,
                                    max_lines=7,
                                    disabled=True
                                ),
                            ],
                            spacing=10,
                            wrap=False,
                            alignment=ft.MainAxisAlignment.START,
                            horizontal_alignment=ft.CrossAxisAlignment.CENTER,
                            width=300
                        )
                    ],
                    spacing=20,
                    wrap=False,
                    alignment=ft.MainAxisAlignment.START,
                    vertical_alignment=ft.CrossAxisAlignment.START
                )
            ],
            spacing=20,
            wrap=False,
            alignment=ft.MainAxisAlignment.CENTER,
            vertical_alignment=ft.CrossAxisAlignment.START
        )
    ]
    
    # Draw Add
    for row in page_grid:
        page.add(row)


