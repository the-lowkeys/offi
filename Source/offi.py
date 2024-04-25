# This module contains the main function and the
# launch point for the program.

# Packages
import sys
import flet as ft

# Project Modules
from Modules.Core import officore as ofc

# Main Function
def main(offi = ft.Page):
    init = ofc.offi_core(sys.argv[1:])

ft.app(main)