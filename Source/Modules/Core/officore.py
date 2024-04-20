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
            print(f"Offi {str.capitalize(core.__version_stage)} {core.__version}")
            print("Development Test Version.\n")
        # Prompt
        core.__page_prompt()

    # Private Methods
    def __load_glob(core):
        # Temporary Global Values, make read function later
        core.__version = '0.0.a1'
        core.__version_stage = 'alpha'
        core.__run_mode = 'cmd'
        core.__app_state = 'menu'

    def __page_prompt(core):
        # CMD 
        if core.__run_mode == 'cmd':
            while (core.__app_state == 'menu'):
                print("Select Program Mode:")
                print("> Archive Request Form")
                print("> Administrator Dashboard")
                print("> Regulator Dashboard")

                core.__set_run_mode(input("\noffi: "))
            core.__switch_page()
        
    def __set_run_mode(core, input):
        comp = ["archive request form",
                "arf",
                "administrator dashboard",
                "ad",
                "regulator dashboard",
                "rd"]
        try: comp = comp.index(str.lower(input))
        except: return False
        if comp == 0 or comp == 1:
            core.__app_state = 'empl'
        if comp == 2 or comp == 3:
            core.__app_state = 'admn'
        if comp == 4 or comp == 5:
            core.__app_state = 'regl'
        else: return False
        return True
    
    def __switch_page(core):
        if core.__app_state == 'empl':
            core.__req_init()
        if core.__app_state == 'admn':
            core.__admn_init()
        if core.__app_state == 'regl':
            core.__regl_init()

    def __parse_args(core, args):
        pass

    def __req_init(core):
        pass

    def __admn_init(core):
        pass

    def __regl_init(core):
        pass

    # Public Methods


    # Test Emulated Transaction
    def test(core):
        pass
    
    