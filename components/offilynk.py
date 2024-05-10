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


    # Interface Functions
    """
    The check_credentials function takes in a set of attributes.
        user-email: str (len <= 50)
        user-key: str (len <= 50)
    Returns false if it doesn't find the employee on the database.
    Otherwise, returns the user-id and user-permission
    """
    def check_credentials(proc, user_attributes: dict):
        if (len(user_attributes['user-email']) > 50) or (len(user_attributes['user-key']) > 50):
            print(user_attributes)
            return False
        query = f'''SELECT * FROM Employees WHERE Email = \'{user_attributes['user-email']}\' AND 
                    EmployeeKey = \'{user_attributes['user-key']}\''''
        user_list = pd.read_sql_query(query, proc.__link)
        print(user_list)
        if user_list.empty:
            return False
        return (user_list.loc[0, 'EmployeeID'], user_list.loc[0, 'EmployeeRole'])
    
    """
    The add_request function takes in a set of attributes.
        file-name: str (len <= 50)
        request-type: str ('QUERY', 'STORE', 'RETRIEVE')
        file-desc: str (len <= 2000)
    """
    def add_request(proc, file_attributes: dict):
        pass

    """
    The process_request function takes in a set of attributes,
    depending on the process type.


    """
    def process_request(proc, type: bool, file_attributes: dict):
        if type:
            pass
        
        pass

    """
    The validate_request function takes in a set of attributes:
    """
    def validate_request(proc, type: bool, file_attributes: dict):
        pass
    
    # Interface Helpers

    def __push_file(proc, ):
        pass

    def __get_employee_requests(proc, ):
        pass


    