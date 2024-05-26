from chessPiece import ChessPiece

class Pawn(ChessPiece):
    def __init__(self, is_white:bool):
        super().__init__("Pawn", is_white)
        self.has_moved = False
        self.is_white =  is_white

    def move (self, is_two_moves:bool):
        if is_two_moves == True:
            print (f"{'White' if self.is_white else 'Black'} pawn has moved two steps")
        else:
            print (f"{'White' if self.is_white else 'Black'} pawn has moved one step")
        self.has_moved=True

    def __str__(self):
        return (f"{'White' if self.is_white else 'Black'} pawn {'has already ' if self.has_moved else 'has not yet '}moved")