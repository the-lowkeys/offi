# This file contains the main core process of the
# offi program. It manages the 

# Package Imports
import flet as ft
import sqlite3 as sql3

# Project Module Import
from components import offilynk as ofl

# Project Pages Import
from components.pages import keeper
from components.pages import login
from components.pages import request
from components.pages import validate

class core: 
    # Constructor
    def __init__(proc, page, args):
        # Type Check Cascade
        if type(page) != ft.Page:
            raise TypeError('Argument \'page\' is not an \'flet.Page\' object!')
        if type(args) != list:
            raise TypeError('Argument \'args\' is not of type \'list\'!')

        # Program Properties Setup
        proc.__PROGRAM_ARGS = {
            '--debug-mode': None
            
        }
        
        proc.__PAGE_LIST = (
            '__LOGIN',
            '__KEEPER',
            '__REQUEST',
            '__VALIDATE'
        )

        proc.__WINDOW = page    # Set as Window

        # Program Process Setup
        proc.__parse_args(args)
        proc.__set_screen('__LOGIN')
        proc.__handler()

    # Program Handler
    def __handler(proc, page):
        # Type Check
        if type(page) != ft.Page:
            raise TypeError('Argument \'page\' is not an \'flet.Page\' object!')
    
        
    # Argument Parser
    def __parse_args(proc, args):
        # Type Check
        if type(args) != list:
            raise TypeError('Argument \'Args\' must be of type \'list\'!') 

    
    # Router Functions
    def change_screen(proc, page_str):
        # Type Check
        if type(page_str) != str:
            raise TypeError('Argument \'page_str\' must be of type \'str\'!')
        
        # In-Screen Check
        if (page_str == proc.__current_page):
            return False

        # Change Screen
        
    def __set_screen(proc, page_str):
        # Type Check
        if type(page_str) != str:
            raise TypeError('Argument \'page_str\' must be of type \'str\'!')
        
        if (page_str == proc.__PAGE_LIST[0]): # Login Page
            login.draw(proc.__WINDOW, debug=proc.__debug_mode)
            proc.__current_page = page_str

        if (page_str == proc.__PAGE_LIST[1]): # Keeper Page
            keeper.draw(proc.__WINDOW)

    