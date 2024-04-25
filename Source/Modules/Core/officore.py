# This module contains the definitions for the core program of offi,
# which handles the transactions and primary  

# Packages
import flet as ft

# Project Modules
from ..Database import offidb as db
"""
from ...Pages.LoginDashboard.logdash import logdash as lgd
from ...Pages.RequestDashboard import reqdash as rqd
from ...Pages.AdminDashboard import adidash as amd
from ...Pages.ValidationDashboard import valdash as vld
"""
# Core Class
class offi_core:
    # Constructor
    def __init__(core, args):
        # Protection Clause
        if type(args) is not list:
            raise TypeError("Argument for parameter \'args\' is not of type \'list\'!")
        
    def __args_mod(core, args):
        pass
        

# Helper Functions
def switch_view(view):
    # Protection Clause
    if type(view) is not ft.View:
        raise TypeError("Argument for parameter \'view\' is not of type \'flet.View\'!")
    
    