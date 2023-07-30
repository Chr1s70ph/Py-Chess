import pygame


class Piece:
    image: pygame.Surface
    color: str
    x_pos: int
    y_pos: int


class Pawn(Piece):
    def __init__(self, color: str, x_pos: int, y_pos: int) -> None:
        self.color = color
        self.x_pos = x_pos
        self.y_pos = y_pos
        self.image = pygame.image.load("./pieces/Chess_plt45.svg") if self.color == "white" else pygame.image.load(
            "./pieces/Chess_pdt45.svg")


class Knight(Piece):
    def __init__(self, color: str, x_pos: int, y_pos: int) -> None:
        self.color = color
        self.x_pos = x_pos
        self.y_pos = y_pos
        self.image = pygame.image.load("./pieces/Chess_nlt45.svg") if self.color == "white" else pygame.image.load(
            "./pieces/Chess_ndt45.svg")


class Rook(Piece):
    def __init__(self, color: str, x_pos: int, y_pos: int) -> None:
        self.color = color
        self.x_pos = x_pos
        self.y_pos = y_pos
        self.image = pygame.image.load("./pieces/Chess_rlt45.svg") if self.color == "white" else pygame.image.load(
            "./pieces/Chess_rdt45.svg")


class Bishop(Piece):
    def __init__(self, color: str, x_pos: int, y_pos: int) -> None:
        self.color = color
        self.x_pos = x_pos
        self.y_pos = y_pos
        self.image = pygame.image.load("./pieces/Chess_blt45.svg") if self.color == "white" else pygame.image.load(
            "./pieces/Chess_bdt45.svg")


class Queen(Piece):
    def __init__(self, color: str, x_pos: int, y_pos: int) -> None:
        self.color = color
        self.x_pos = x_pos
        self.y_pos = y_pos
        self.image = pygame.image.load("./pieces/Chess_qlt45.svg") if self.color == "white" else pygame.image.load(
            "./pieces/Chess_qdt45.svg")


class King(Piece):
    def __init__(self, color: str, x_pos: int, y_pos: int) -> None:
        self.color = color
        self.x_pos = x_pos
        self.y_pos = y_pos
        self.image = pygame.image.load("./pieces/Chess_klt45.svg") if self.color == "white" else pygame.image.load(
            "./pieces/Chess_kdt45.svg")
