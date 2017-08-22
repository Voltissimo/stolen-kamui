from game import Board, Piece
from typing import Tuple, Union


std_board = Board.create_standard_board()


def current_player_points(board: 'Board') -> float:

    if board.current_player.is_in_checkmate():
        return int('+inf')

    material_bonus = \
        sum([i.PIECE_VALUE for i in board.current_player.active_pieces]) - \
        sum([i.PIECE_VALUE for i in board.current_player.get_opponent().active_pieces])

    pawn_row = 2 if board.current_player.color == 'WHITE' else 7

    for col in ['d', 'e']:
        print(board)

    # development_bonus = 0
    #

    return material_bonus


def minimax(current_board: 'Board', depth: int, maximizing: bool) -> Tuple[float, Union['Piece', None]]:
    if depth == 0 or current_board.current_player.is_in_checkmate():
        return current_player_points(current_board), None

    if maximizing:
        best_score = float('-inf')
        best_move = None

        for legal_move in current_board.current_player.calculate_legal_moves():
            new_board = legal_move.execute()
            move_value, move_obj = minimax(new_board, depth - 1, False)

            if best_score < move_value:
                best_score = move_value
                best_move = legal_move

        return best_score, best_move

    else:
        best_score = float('+inf')
        best_move = None

        for legal_move in current_board.current_player.calculate_legal_moves():
            new_board = legal_move.execute()
            move_value, move_obj = minimax(new_board, depth - 1, True)

            if move_value < best_score:
                best_score = move_value
                best_move = legal_move

        return best_score, best_move

print(minimax(std_board, 2, True)[1])


