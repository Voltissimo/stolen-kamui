from game import Board, Move
from typing import Tuple, Union


def current_player_points(board: 'Board') -> float:
    if board.current_player.is_in_checkmate():
        return float('+inf')

    board_eval = 0
    # material
    board_eval += \
        sum([i.PIECE_VALUE for i in board.current_player.active_pieces]) - \
        sum([i.PIECE_VALUE for i in board.current_player.get_opponent().active_pieces])
    pawn_row = 2 if board.current_player.color == 'WHITE' else 7
    if not all([board[col + str(pawn_row)] for col in ['d', 'e']]):
        board_eval += 1

    return board_eval


def minimax(current_board: 'Board', depth: int, maximizing: bool) -> Tuple[float, Union['Move', None]]:
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

DEPTH = 2
current_board = Board.create_standard_board()

while True:
    _, white_move = minimax(current_board, DEPTH, True)
    current_board = white_move.execute()
    print(current_board)
    print(_)
    input()
    _, black_move = minimax(current_board, DEPTH, True)
    current_board = black_move.execute()
    for i in current_board.current_player.calculate_legal_moves():
        print(i)
    print(current_board)
    print(_)
    input()
