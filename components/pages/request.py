# Package Imports
import pandas as pd
import flet as ft
from functools import partial

# Requestor Page Method Call
def draw(page, debug=False, handlers: dict=None):
    # Type Check
    if type(page) != ft.Page:
        raise TypeError('Argument \'page\' is not an \'flet.Page\' object!')
    
    # Alias
    __db = handlers['lynk']

    # Functions
    def unfocus_strip(e):
        page_grid[1].controls[1].value = page_grid[1].controls[1].value.strip()
        page.update()
    
    def __get_datagrid(row: int, col: int, e):
        if (row < 0) or (row > 6) or (col < 0) or (col > 2):
            raise ValueError('\'row\' or \'col\' out of bounds!')
                       # Grid   # 3rd Row   # 1st Row   # DataTable        # DataGrid Col
        transaction_id=page_grid[2].controls[0].controls[0].rows[row].cells[col].content.value
                                                                # DataGrid Row           # Cell Text
        if transaction_id == '': return False
        __update_fields(__db.get_transaction_attr(int(transaction_id)))        
    
    def __update_datagrid():
        __clear_datagrid()
        transactions = __db.get_employee_transactions()

        pass

    def __set_datagrid(row: int, col: int, value: str=''):
        if (row < 0) or (row > 6) or (col < 0) or (col > 2):
            raise ValueError('\'row\' or \'col\' out of bounds!')
        # Grid   # 3rd Row   # 1st Row   # DataTable        # DataGrid Col
        page_grid[2].controls[0].controls[0].rows[row].cells[col].content.value = value
                                                 # DataGrid Row           # Cell Text

    def __clear_datagrid():
        for idx_r in range(0, 7, 1):
            for idx_c in range(0, 3, 1):
                __set_datagrid(idx_r, idx_c)

    def __update_fields(transaction_attr: pd.DataFrame):
        
        pass

    def __clear_fields(e, field: str):
        pass

    def __field_clean(e):
        
        pass

    def refresh(e):
        __update_datagrid()
        pass

    def __return(e):
        handlers['change-screen']('__LOGIN')

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
                                    on_long_press=partial(__get_datagrid, 0, 0)
                                ),
                                ft.DataRow(
                                    cells=[
                                        ft.DataCell(ft.Text('')),
                                        ft.DataCell(ft.Text('')),
                                        ft.DataCell(ft.Text(''))
                                    ],
                                    on_long_press=partial(__get_datagrid, 1, 0)
                                ),
                                ft.DataRow(
                                    cells=[
                                        ft.DataCell(ft.Text('')),
                                        ft.DataCell(ft.Text('')),
                                        ft.DataCell(ft.Text(''))
                                    ],
                                    on_long_press=partial(__get_datagrid, 2, 0) 
                                ),
                                ft.DataRow(
                                    cells=[
                                        ft.DataCell(ft.Text('')),
                                        ft.DataCell(ft.Text('')),
                                        ft.DataCell(ft.Text(''))
                                    ],
                                    on_long_press=partial(__get_datagrid, 3, 0)   
                                ),
                                ft.DataRow(
                                    cells=[
                                        ft.DataCell(ft.Text('')),
                                        ft.DataCell(ft.Text('')),
                                        ft.DataCell(ft.Text(''))
                                    ],
                                    on_long_press=partial(__get_datagrid, 4, 0)   
                                ),
                                ft.DataRow(
                                    cells=[
                                        ft.DataCell(ft.Text('')),
                                        ft.DataCell(ft.Text('')),
                                        ft.DataCell(ft.Text(''))
                                    ],
                                    on_long_press=partial(__get_datagrid, 5, 0)   
                                ),
                                ft.DataRow(
                                    cells=[
                                        ft.DataCell(ft.Text('')),
                                        ft.DataCell(ft.Text('')),
                                        ft.DataCell(ft.Text(''))
                                    ],
                                    on_long_press=partial(__get_datagrid, 6, 0)   
                                )
                            ],
                            column_spacing=5,
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
                                            text='Back',
                                            on_click=__return
                                        ),
                                        ft.TextButton(
                                            text='Refresh',
                                            on_click=refresh
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