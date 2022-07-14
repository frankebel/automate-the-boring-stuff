#!/usr/bin/env python
import re

def isValidChessBoard(board):
    # Check for king.
    for king in ('wking', 'bking'):
        if list(board.values()).count(king) != 1:
            return False

    # Maximum of 16 pieces.
    for color in (re.compile("^w"), re.compile("^b")):
        if len(list(filter(color.search, board))) > 16:
            return False

    # Maximum of 8 pawns.
    for pawn in ('wpawn', 'bpawn'):
        if list(board.values()).count(pawn) > 8:
            return False
    
    # Space must be from '1a' to '8h'.
    r = re.compile("^[1-8][a-h]$")
    if len(list(filter(r.search, board))) != len(board.values()):
        return False

    # Check all piece names.
    r = re.compile("^[wb](pawn|knight|bishop|rook|queen|king)$")
    if len(list(filter(r.search, board.values()))) != len(board.values()):
        return False

    return True


board = {'1h': 'bking', '6c': 'wqueen', '2g': 'bbishop', '5h': 'bqueen', '3e': 'wking'}
print(isValidChessBoard(board))

