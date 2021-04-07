"""
Device access types according Thyracont's Protocol
"""

class AccessCode():
    RD_TX = 0
    RD_RX = 1
    WR_TX = 2
    WR_RX = 3
    DEF_TX = 4
    DEF_RX = 5
    ERR_TX = None
    ERR_RX = 7
    BIN_TX = 8
    BIN_RX = 9
