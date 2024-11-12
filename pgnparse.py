import chess.pgn

with open("out.pgn") as pgn:
    for i in range(100):
        first_game = chess.pgn.read_game(pgn)

        
        board = first_game.board()
        for move in first_game.mainline_moves():
            board.push(move)
            # print(board, "\n")
            # print(board.is_check())
        print(board.outcome())