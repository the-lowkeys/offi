# This file contains the main

# Package Imports
import sys
import flet as ft

# Project Module Imports
from components import officore as ofc

# Main Function
def main(offi: ft.Page):
    # Initialization Step
    core_process = ofc.core(offi, sys.argv)

ft.app(main)
