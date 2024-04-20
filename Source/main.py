# This module contains the main function and the
# launch point for the program.

# Packages
import sys

# Project Modules
from Modules.Core import officore as ofc

# Main Function
def main():
    init = ofc.officore(sys.argv[1:])

if __name__ == '__main__':
    main()