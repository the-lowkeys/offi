# This module contains the definitions for the core program of offi,
# which handles the transactions  

# Packages

# Project Modules

#   
class officore:
    # Constructors and Specials
    def __init__(core, args):
        # Boot Core
        core.__load_glob()
        if len(args): core.__parse_args(args)
        if core.__run_mode == 'cmd':
            print(f"Offi {str.capitalize(core.__version_stage)} {core.__version}\n")
            print("Development Test Version")
        # Prompt
        core.__page_prompt()

    # Private Methods
    def __load_glob(core):
        # Temporary Global Values, make read function later
        core.__version = '0.0.a1'
        core.__version_stage = 'alpha'
        core.__run_mode = 'cmd'

    def __page_prompt(core):
        # CMD 
        if core.__run_mode == 'cmd':
            print()

    def __parse_args(core, args):
        pass

    # Public Methods


    # Test Emulated Transaction
    def test(core):
        pass
    
    