# This module contains the definitions for the core program of offi,
# which handles the transactions and primary  

# Packages
import flet as ft

# Project Modules
from ..Database import offidb as db

from ...Pages.LoginDashboard import logdash as lgd
from ...Pages.RequestDashboard import reqdash as rqd
from ...Pages.AdminDashboard import adidash as amd
from ...Pages.ValidationDashboard import valdash as vld

# Core Class
class offi_core:
    def __init__(core, args, page):
        # Exception Cascade
        if type(args) is not list:
            raise TypeError("Argument for parameter \'args\' is not an argument list!")
        pass

# Helper Functions
def switch_view(view):
    pass
    
    