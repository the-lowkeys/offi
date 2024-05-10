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
    
    # Interface Helpers
    # # File Functions
    def check_file(proc, file_name: str):
        if (type(file_name) != str) or (len(file_name) > 50): return False
        query = f'SELECT * FROM Files WHERE FileLabel = \'{file_name}\''
        result = pd.read_sql_query(query, proc.__link)
        
        if result.empty:
            return False
        
        # Guaranteed to be Unique
        return (result.loc[0, 'FileID'], result.loc[0, 'DrawerID'])
    
    def get_file_attr(proc, file_id: int):
        if (type(file_id) != int): return False
        query = f'SELECT * FROM Files WHERE FileID = \'{str(file_id)}\''
        result = pd.read_sql_query(query, proc.__link)
        if result.empty:
            return False
        
        # Guarranteed to be Unique
        return result

    # # Drawer Functions
    def check_drawer(proc, drawer_name: str):
        if (type(drawer_name) != str) or (len(drawer_name) > 50): return False
        query = f'SELECT * FROM Drawers WHERE DrawerLabel = \'{drawer_name}\''
        result = pd.read_sql_query(query, proc.__link)

        if result.empty:
            return False
        
        # Not Guaranteed to be Unique
        return pd.concat(result['DrawerID'], result['CabinetID'])
    
    def get_drawer_attr(proc, drawer_id: int):
        if (type(drawer_id) != int): return False
        query = f'SELECT * FROM Drawers WHERE DrawerID = \'{str(drawer_id)}\''
        result = pd.read_sql_query(query, proc.__link)

        if result.empty:
            return False
        
        # Not Guaranteed to be Unique
        return result
    
    def get_drawer_files(proc, drawer_id: int):
        if (type(drawer_id) != int): return False
        query = f'SELECT FileID FROM Files WHERE DrawerID = \'{str(drawer_id)}\''
        result = pd.read_sql_query(query, proc.__link)

        if result.empty:
            return False
        
        # Not Guaranteed to be Unique
        return result['FileID']
    
    # # Cabinet Functions
    def check_cabinet(proc, cabinet_name:str):
        pass

    def get_cabinet_attr(proc, cabinet_id: int):
        pass

    # # Transaction Functions
    def get_status_files(proc, transaction_status: str):
        if (type(transaction_status) != str) or (len(transaction_status) > 9):
            return False
        query = f'SELECT * FROM Transactions WHERE Status = \'{transaction_status}\''
        result = pd.read_sql_query(query, proc.__link)

        if result.empty:
            return False
        
        # Not Unique
        return result
    
    def get_transaction_attr(proc, transaction_id: int):
        if (type(transaction_id) != int):
            return False
        query = f'SELECT * FROM Transactions WHERE TransactionID = \'{str(transaction_id)}\''
        result = pd.read_sql_query(query, proc.__link)

        if result.empty:
            return False
        
        # Not Unique
        return result
    
    def get_employee_transactions(proc):
        pass
        
        

    