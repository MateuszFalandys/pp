# 8 x 8

#     A B C D E F G H
#   1 # # # # # # # #
#   2 # # # # # # # #
#   3 # # # # # # # #
#   4 # # # # # # # #
#   5 # # # # # # # #
#   6 # # # # # # # #
#   7 # # # # # # # #
#   8 # # # # # # # #

WHITE_PAWN = "WP"
BLACK_PAWN = "BP"

chess_row = ["--" for i in range(8)]
chessboard = [chess_row[:] for i in range(8)]

chessboard[0][0] = WHITE_PAWN
chessboard[3][5] = BLACK_PAWN

for chess_row in chessboard:
    for chess_square in chess_row:
        print(chess_square, end=" ")
    print()

