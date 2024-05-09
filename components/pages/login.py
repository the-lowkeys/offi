# This file

# Package Imports
import flet as ft

# Login Page Values

# Login Page Method Call
def draw(page, debug=False):
    # Type Check
    if type(page) != ft.Page:
        raise TypeError('Argument \'page\' is not an \'flet.Page\' object!')
    
    # Draw Screen
    page.add(ft.TextButton('Click Me!'))

def get_info():
    pass
    