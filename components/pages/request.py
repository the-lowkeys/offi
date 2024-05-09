# This file

# Package Imports
import flet as ft

# Requestor Page Method Call
def draw(page, debug=False, handlers: tuple=None):
    # Type Check
    if type(page) != ft.Page:
        raise TypeError('Argument \'page\' is not an \'flet.Page\' object!')
    if type(handlers) != None:
        if type(handlers) != tuple:
            raise TypeError('Argument \'handlers\' is not of type \'tuple\'')
        
    # Draw Screen
    
    
    