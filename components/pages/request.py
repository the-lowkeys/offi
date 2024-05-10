# Package Imports
import flet as ft

# Requestor Page Method Call
def draw(page, debug=False, handlers: dict=None):
    # Type Check
    if type(page) != ft.Page:
        raise TypeError('Argument \'page\' is not an \'flet.Page\' object!')
        
    # Draw Screen
    page.window_resizable = True
    txt = ft.Text(value="Request Form", text_align=ft.TextAlign.LEFT, width=500, size=50)
    page.add(txt)
    
    def button_clicked(e):
        t.value = f"Dropdown value is:  {dd.value}, Text field value is: {tf.value}"
        page.update()

    t = ft.Text()
    b = ft.ElevatedButton(text="Submit", on_click=button_clicked)
    dd = ft.Dropdown(
        width=300,
        options=[
            ft.dropdown.Option("Retrieve"),
            ft.dropdown.Option("Store"),
            ft.dropdown.Option("Query"),
        ],
        
    )
    tf = ft.TextField(label='File Name')  # Add this line to create a TextField
    tf2 = ft.TextField(label="Description", multiline=True, min_lines=10, max_lines=20)
    # Create a Row widget and add the Dropdown and TextField to it
    row = ft.Row([dd, tf])

    # Add the Row, Button, and Text to the page
    page.add(row, t, tf2, b)

def get_info():
    pass