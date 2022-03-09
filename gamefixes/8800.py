""" Sid Meier's Civilization IV: Beyond the Sword
"""

# Note: as of 2022-mar-07 buttons glitchy unless using PROTON_USE_WINED3D=1 environment

from protonfixes import util

def main():

    util.protontricks('msxml3')
    util.protontricks('corefonts')
    util.disable_dxvk()
    
