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
            return False
        query = f'''SELECT * FROM Employees WHERE Email = \'{user_attributes['user-email']}\' AND 
                    EmployeeKey = \'{user_attributes['user-key']}\''''
        user_list = pd.read_sql_query(query, proc.__link)
        if user_list.empty:
            return False
        # Guaranteed to be Unique
        return (user_list.loc[0, 'EmployeeID'], user_list.loc[0, 'EmployeeRole'])
    
    """
    The update_transaction function takes in a set of attributes.
        type: True (add/update) or False (remove)
    Attributes:
        file-name: str (len <= 50)
        request-type: str ('QUERY', 'STORE', 'RETRIEVE')
        file-desc: str (len <= 2000)
        request-status: str ('REQUESTED', 'ACCEPTED', 'REJECTED', 'VALIDATED', 'CANCELLED')
    Modifies files stored in Heap.
    """
    def update_transaction(proc, type: bool, file_attributes: dict):
        # Check if File Exists first

        pass

    """
    The process_transaction function takes in a set of attributes.
        type: True (accept) or False (reject)
    Attributes:
        


    """
    def process_transaction(proc, type: bool, file_attributes: dict):
        if type:
            pass
        
        pass

    """
    The validate_transaction function takes in a set of attributes:
    """
    def validate_transaction(proc, type: bool, file_attributes: dict):
        pass
    
    # Interface Helpers
    def __check_file(proc, file_name: str):
        if (type(file_name) != str) or (len(file_name) > 50): return False
        query = f'SELECT * FROM Files WHERE FileLabel = \'{file_name}\''
        result = pd.read_sql_query(query, proc.__link)
        
        if result.empty:
            return False
        
        # Guaranteed to be Unique
        return (result.loc[0, 'FileID'], result.loc[0, 'DrawerID'])
    
    def __get_file_attr(proc, file_id: str):
        if (type(file_id) != str) or (len(file_id) > 50): return False
        query = f'SELECT * FROM Files WHERE FileID = \'{file_id}\''
        result = pd.read_sql_query(query, proc.__link)
        if result.empty:
            return False
        
        # Guarranteed to be Unique
        return result

    def __check_drawer(proc, drawer_name: str):
        if (type(drawer_name) != str) or (len(drawer_name) > 50): return False
        query = f'SELECT * FROM Drawers WHERE DrawerLabel = \'{drawer_name}\''
        result = pd.read_sql_query(query, proc.__link)

        if result.empty:
            return False
        
        # Not Guaranteed to be Unique
        return pd.concat(result['DrawerID'], result['CabinetID'])
    
    def __get_drawer_attr(proc, drawer_id: str):
        if (type(drawer_id) != str) or (len(drawer_id) > 50): return False
        query = f'SELECT * FROM Drawers WHERE DrawerID = \'{drawer_id}\''
        result = pd.read_sql_query(query, proc.__link)

        if result.empty:
            return False
        
        # Not Guaranteed to be Unique
        return result
    
    def __get_drawer_files(proc, drawer_id: str):
        if (type(drawer_id) != str) or (len(drawer_id) > 50): return False
        query = f'SELECT * FROM Files WHERE DrawerID = \'{drawer_id}\''
        result = pd.read_sql_query(query, proc.__link)

        if result.empty:
            return False
        
        # Not Guaranteed to be Unique
        return result['FileID']

    