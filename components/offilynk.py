# This file contains

# Package Imports
from os import mkdir
from os.path import exists
from functools import partial
import sqlite3 as sql3
import pandas as pd

# Class
class lynk:
    # Constructor
    def __init__(proc):
        # Class Properties Setup
        proc.__DB_PATH = 'data/offi.db'
        if exists(proc.__DB_PATH):
            proc.__db_init_mode = False
        else:
            proc.__db_init_mode = True
            mkdir('data')
        proc.__link = sql3.connect(proc.__DB_PATH)
    
        # # Initialize Class
        proc.__db_init()

    # Database Initializer
    def __db_init(proc):
        proc.__editor = proc.__link.cursor()
        if proc.__db_init_mode:
            script_paths = (
            'scripts/empl_mockdata.sql',
            'scripts/emplself_mockdata.sql',
            'scripts/crud_tables.sql'
            )
            print('hello', proc.__db_init_mode)
            for path in script_paths:
                script = open(path, 'r')
                queries = script.read().split(';')
                for query in queries:
                    query += ';'
                    proc.__editor.execute(query)
                    query = ''
                script.close()
            proc.__link.commit()
        # Post-Init


    # Exposed Functions
    def add_request(proc, file_attributes: dict):
        pass

    def check_credentials(proc, user_attributes: dict):
        pass

    