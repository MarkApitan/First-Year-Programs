from chessPiece import ChessPiece
from pawn import Pawn
white_pawn = Pawn(True)
print(white_pawn)  # White pawn has not yet moved
white_pawn.move(False)  # White pawn has moved one step
print(white_pawn)  # White pawn has already moved

# Creating a black pawn
black_pawn = Pawn(False)
print(black_pawn)  # Black pawn has not yet moved
black_pawn.move(True)  # Black pawn has moved two steps
print(black_pawn)  # Black pawn has already moved