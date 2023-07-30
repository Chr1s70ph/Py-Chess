import pygame
import pieces

resolution = (800, 800)
screen = pygame.display.set_mode(resolution)
map_size = (8, 8)  # (rows, columns)
line_width = 1
clock = pygame.time.Clock()  # to set max FPS
starting_map = "rnbqkbnrpppppppp00000000000000000000000000000000PPPPPPPPRNBQKBNR"


square_width = (resolution[0] / map_size[0]) - \
    line_width * ((map_size[0] + 1) / map_size[0])

square_height = (resolution[1] / map_size[1]) - \
    line_width * ((map_size[1] + 1) / map_size[1])

# def evaluate_dimensions():
#     # Evaluate the width and the height of the squares.
#     square_width = (resolution[0] / map_size[0]) - \
#         line_width * ((map_size[0] + 1) / map_size[0])
#     square_height = (resolution[1] / map_size[1]) - \
#         line_width * ((map_size[1] + 1) / map_size[1])
#     return (square_width, square_height)


def convert_column_to_x(column, square_width):
    x = line_width * (column + 1) + square_width * column
    return x


def convert_row_to_y(row, square_height):
    y = line_width * (row + 1) + square_height * row
    return y


def draw_squares():
    # square_width, square_height = evaluate_dimensions()
    for row in range(map_size[0]):
        for column in range(map_size[1]):
            # fancy counting for chessboard colors
            cnt = (row * map_size[0]) + \
                (column if (row % 2 == 0) else column - 1)
            color = (255, 255, 255) if cnt % 2 == 0 else (100, 100, 100)
            x = convert_column_to_x(column, square_width)
            y = convert_row_to_y(row, square_height)
            geometry = (x, y, square_width, square_height)
            pygame.draw.rect(screen, color, geometry)


def display_piece(_piece_name, color, x, y, square_width, square_height):
    if _piece_name.lower() == "p":
        p = pieces.Pawn(color, x, y)
        screen.blit(p.image, (x * square_width, y * square_height))
    if _piece_name.lower() == "r":
        p = pieces.Rook(color, x, y)
        screen.blit(p.image, (x * square_width, y * square_height))
    if _piece_name.lower() == "n":
        p = pieces.Knight(color, x, y)
        screen.blit(p.image, (x * square_width, y * square_height))
    if _piece_name.lower() == "b":
        p = pieces.Bishop(color, x, y)
        screen.blit(p.image, (x * square_width, y * square_height))
    if _piece_name.lower() == "q":
        p = pieces.Queen(color, x, y)
        screen.blit(p.image, (x * square_width, y * square_height))
    if _piece_name.lower() == "k":
        p = pieces.King(color, x, y)
        screen.blit(p.image, (x * square_width, y * square_height))


def populate_board():
    cnt = 0
    for piece in starting_map:
        cnt += 1
        if piece == "0":
            continue

        x = convert_column_to_x(cnt % 8, square_width)
        y = convert_row_to_y(int((cnt - 1) / 8), square_height)
        color = "white" if piece.isupper() else "black"
        display_piece(piece, color, cnt % 8, int(
            (cnt - 1) / 8), square_width, square_height)


draw_squares()
populate_board()

while True:
    clock.tick(15)  # max FPS = 15
    pygame.display.flip()  # Update the screen.
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            quit()
