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
                ft.Text('Request Form', 
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
                ft.Dropdown(
                    value='Store',
                    options=[
                        ft.dropdown.Option('Store'),
                        ft.dropdown.Option('Retrieve'),
                        ft.dropdown.Option('Query')
                    ],
                    on_change=selective_enable,
                    width=250
                ),
                ft.TextField(
                    label='File Name',
                    on_blur=unfocus_strip,
                    width=450
                )
                
            ],
            spacing=20,
            wrap=False,
            alignment=ft.MainAxisAlignment.CENTER,
            vertical_alignment=ft.CrossAxisAlignment.START
        ),
        ft.Row(
            [
                ft.Row(
                    [
                        ft.DataTable(
                            columns=[
                                ft.DataColumn(
                                    ft.Text('Transaction ID'),
                                    tooltip='Unique Transaction ID'
                                ),
                                ft.DataColumn(
                                    ft.Text('File Name'),
                                    tooltip='Unique File Name'
                                ),
                                ft.DataColumn(
                                    ft.Text('Status'),
                                    tooltip='Transaction Status'
                                )
                            ],
                            rows=[
                                ft.DataRow(
                                    cells=[
                                        ft.DataCell(ft.Text('')),
                                        ft.DataCell(ft.Text('')),
                                        ft.DataCell(ft.Text(''))
                                    ],
                                    on_select_changed=radio_select
                                ),
                                ft.DataRow(
                                    cells=[
                                        ft.DataCell(ft.Text('')),
                                        ft.DataCell(ft.Text('')),
                                        ft.DataCell(ft.Text(''))
                                    ],
                                    on_select_changed=radio_select
                                ),
                                ft.DataRow(
                                    cells=[
                                        ft.DataCell(ft.Text('')),
                                        ft.DataCell(ft.Text('')),
                                        ft.DataCell(ft.Text(''))
                                    ],
                                    on_select_changed=radio_select
                                ),
                                ft.DataRow(
                                    cells=[
                                        ft.DataCell(ft.Text('')),
                                        ft.DataCell(ft.Text('')),
                                        ft.DataCell(ft.Text(''))
                                    ],
                                    on_select_changed=radio_select
                                ),
                                ft.DataRow(
                                    cells=[
                                        ft.DataCell(ft.Text('')),
                                        ft.DataCell(ft.Text('')),
                                        ft.DataCell(ft.Text(''))
                                    ],
                                    on_select_changed=radio_select
                                ),
                                ft.DataRow(
                                    cells=[
                                        ft.DataCell(ft.Text('')),
                                        ft.DataCell(ft.Text('')),
                                        ft.DataCell(ft.Text(''))
                                    ],
                                    on_select_changed=radio_select
                                ),
                                ft.DataRow(
                                    cells=[
                                        ft.DataCell(ft.Text('')),
                                        ft.DataCell(ft.Text('')),
                                        ft.DataCell(ft.Text(''))
                                    ],
                                    on_select_changed=radio_select
                                )
                            ],
                            column_spacing=5,
                            show_checkbox_column=True,
                            checkbox_horizontal_margin=10,
                            divider_thickness=0,
                            width=400
                        ),
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

