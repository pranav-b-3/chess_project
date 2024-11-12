import chess.pgn


import numpy as np

def fen_to_numpy(fen):
    pieces = []
    piece_to_pos = {}
    i = 0
    for piece in 'PNBRQKpnbrqk':
        piece_to_pos[piece] = i
        i += 1
    for piece in 'PNBRQKpnbrqk':
        pieces.append(np.zeros((8, 8), dtype=bool))
    
    board_fen = fen.split()[0]
    
    rank_idx = 0
    for rank in board_fen.split('/'):
        file_idx = 0
        for char in rank:
            if char.isdigit():
                file_idx += int(char)
            else:
                pos = piece_to_pos[char]
                pieces[pos][rank_idx, file_idx] = True
                file_idx += 1
        rank_idx += 1
    
    return np.array(pieces)

def print_board(position):
    """Helper function to visualize the position"""
    board = np.full((8, 8), '.')
    for piece, arr in position.items():
        board[arr] = piece
    for rank in board:
        print(' '.join(rank))

start_fen = "rnbqkbnr/pppppppp/8/8/8/8/PPPPPPPP/RNBQKBNR w KQkq - 0 1"
position = fen_to_numpy(start_fen)

print(position.shape)


# print(position['p'])
# print(position['P'])

# # Example of accessing specific pieces
# print("White pawns:")
# print(position['P'].astype(int))
# print("\nBlack knights:")
# print(position['n'].astype(int))

# print("\nComplete board visualization:")
# print_board(position)

# # Test with a more complex position
# mid_game_fen = "r1bqk2r/pppp1ppp/2n2n2/2b1p3/2B1P3/2NP1N2/PPP2PPP/R1BQK2R"
# mid_position = fen_to_numpy(mid_game_fen)
# print("\nMid-game position:")
# print_board(mid_position)


with open("out.pgn") as pgn:
    inputs = []
    outputs = []
    for i in range(1000):
        first_game = chess.pgn.read_game(pgn)

        
        board = first_game.board()
        # print(fen_notation)
        # print(fen_np)
        # exit()
        

        for move in first_game.mainline_moves():
            input_board = fen_to_numpy(board.fen())
            board.push(move)
            output_board = fen_to_numpy(board.fen())
            inputs.append(input_board)
            outputs.append(output_board)
            
            # print(board, "\n")
            # print(board.is_check())
        # print(board.outcome())
    print(len(inputs), len(outputs))