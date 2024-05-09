# This file contains the main core process of the
# offi program. It manages the 

# Package Imports
from functools import partial
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
    def __init__(proc, page: ft.Page, args: list):
        # Type Check Cascade
        if type(page) != ft.Page:
            raise TypeError('Argument \'page\' is not an \'flet.Page\' object!')
        if type(args) != list:
            raise TypeError('Argument \'args\' is not of type \'list\'!')

        # Program Properties Setup
        proc.__WINDOW = page                    # Set as Window
        proc.__WINDOW.window_min_height = 480
        proc.__WINDOW.window_min_width = 800
        proc.__properties = {
            'debug-mode': False,
            'disable-login': False,
            'version': '0.1-alpha'
        }
        proc.__WINDOW.title = 'OFFI v' + proc.__properties['version']
        
        """
        The dictionary __PROGRAM_ARGS is an implementation of a complex enum
        that has its values in a particular tuple format:
            [0]     Partial Function that sets the flag or property
            [1]     Process Property that will be modified
            [2:]    Acceptable Parameters, which can be:
                    None                    Signifies a flag whose state can only be inverted at
                                            start time, depending on the executable argument.
                    type(var)               Signifies only accepting a particular type but with
                                            any value.
                    param1, param2, ...     Signifies the only acceptable parameters for the
                                            property.
        """
        proc.__PROGRAM_ARGS = {                     
            '--debug': (partial(proc.__set_properties, 'debug-mode'),
                        'debug-mode',
                        None
                       ),
            '--skip-login': (partial(proc.__set_properties, 'disable-login'),
                             'disable-login',
                             None
                            )
        }
        
        proc.__PAGE_LIST = {
            '__LOGIN': login.draw,
            '__KEEPER': keeper.draw,
            '__REQUEST': request.draw,
            '__VALIDATE': validate.draw
        }

        # Program Process Setup
        proc.__parse_args(args[1:])
        proc.__set_screen('__LOGIN')
        proc.__handler()

    # Program Handler
    def __handler(proc):     
        
        pass
        
    # Properties and Argument Parser
    def __parse_args(proc, args: list):
        # Type Check
        if type(args) != list:
            raise TypeError('Argument \'Args\' must be of type \'list\'!')
        
        # Argument Parse Cascade
        for key in proc.__PROGRAM_ARGS.keys():
            if key in args:
                loc_arg = args.index(key)
            else: continue

            # Flag Options
            if proc.__PROGRAM_ARGS[args[loc_arg]][2] == None:
                proc.__PROGRAM_ARGS[args[loc_arg]][0](not proc.__get_properties(proc.__PROGRAM_ARGS[args[loc_arg]][1]))

            # TODO: Multi-valued Options
    
    def __set_properties(proc, key: str, val):
        # Type Check
        if type(key) != str:
            raise TypeError('Argument \'key\' must be of type \'str\'!')
        
        # Set Value
        proc.__properties[key] = val     
    
    def __get_properties(proc, key: str):
        # Type Check
        if type(key) != str:
            raise TypeError('Argument \'key\' must be of type \'str\'!')
        
        # Get Value
        return proc.__properties[key]

    # Router Functions
    def __set_screen(proc, page_str: str):
        # Type Check
        if type(page_str) != str:
            raise TypeError('Argument \'page_str\' must be of type \'str\'!')
        
        # Set Screen
        proc.__PAGE_LIST[page_str](proc.__WINDOW, debug=proc.__get_properties('debug-mode'))    
        proc.__current_page = page_str
    
    def change_screen(proc, page_str: str) -> bool:
        # Type Check
        if type(page_str) != str:
            raise TypeError('Argument \'page_str\' must be of type \'str\'!')
        
        # In-Screen Check
        if (page_str == proc.__current_page):
            return False

        # Change Screen
        proc.__WINDOW.controls.clear()
        proc.__set_screen(page_str)
        proc.__WINDOW.update()
        return True
