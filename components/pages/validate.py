# Package Imports
import flet as ft
from time import sleep

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
    
    
    # Draw Screen
    page_grid = [
        ft.Row(
            [
                ft.Text('Validate', 
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
                            ft.Text(value="Accept",
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
                            ft.Text(value="Reject", 
                                    size=13,
                                    ),
                            ],
                            alignment=ft.MainAxisAlignment.CENTER
                        ),
                    )
                ),
                ft.TextField(
                    label='type',
                    width=300,
                    height=100,
                    multiline=True,
                    min_lines=6,
                    max_lines=6
                ),
                
            ],
            spacing=20,
            wrap=False,
            alignment=ft.MainAxisAlignment.SPACE_EVENLY,
            vertical_alignment=ft.CrossAxisAlignment.CENTER
        ),
        ft.Row(
            [
                ft.Row(
                    [
                        ft.Column([
                             ft.TextField(
                            label='drawer'    
                        ),
                        ft.TextField(
                            label='cabinet'    
                        ),
                        ]),
                        
                        ft.Column(
                            [
                                ft.TextField(
                                    label='File Description',
                                    multiline=True,
                                    min_lines=6,
                                    max_lines=6
                                ),
                                ft.TextField(
                                    label='Transaction Comment',
                                    multiline=True,
                                    min_lines=6,
                                    max_lines=6,
                                    disabled=True
                                ),
                                ft.Row(
                                    [
                                        ft.TextButton(
                                            text='Submit'
                                        ),
                                        ft.TextButton(
                                            text='Cancel'
                                        )
                                    ],
                                    spacing=10,
                                    wrap=False,
                                    alignment=ft.MainAxisAlignment.CENTER,
                                    vertical_alignment=ft.CrossAxisAlignment.START
                                )
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


