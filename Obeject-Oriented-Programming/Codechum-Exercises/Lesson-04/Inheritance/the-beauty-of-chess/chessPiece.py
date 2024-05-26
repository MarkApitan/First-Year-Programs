class ChessPiece:
    def __init__(self, type:str, is_white:bool):
        self.type = type
        self.is_white = is_white

    def get_type(self):
        return self.type
    def get_is_white(self):
        return self.is_white