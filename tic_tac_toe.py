"""
Monte Carlo Tic-Tac-Toe Player
"""

# Constants for Monte Carlo simulator
# Change as desired
NTRIALS = 10  # Number of trials to run
SCORE_CURRENT = 1.0  # Score for squares played by the current player
SCORE_OTHER = 1.0  # Score for squares played by the other player


def mc_trial(board, player):
    """
    This function takes a current board and the next player to move.
    The function should play a game starting with the given player by making random moves,
    alternating between players. The function should return when the game is over.
    The modified board will contain the state of the game, so the function does not return anything.
    """
    # for i in range(0, NTRIALS):

    # play an entire game
    # randomly choose move for each player

    curplayer = player
    winner = None
    while winner == None:
        empty_squares = board.get_empty_squares()
        number_empty = len(empty_squares)
        row, col = empty_squares[random.randrange(number_empty)]
        board.move(row, col, curplayer)
        winner = board.check_win()
        curplayer = provided.switch_player(curplayer)


def mc_update_scores(scores, board, player):
    """
    This function takes a grid of scores (a list of lists) with the same dimensions
    as the Tic-Tac-Toe board, a board from a completed game, and which player the
    machine player is. The function should score the completed board and update the scores grid.
    As the function updates the scores grid directly, it does not return anything,
    """
    winner = board.check_win()

    for col in range(board.get_dim()):
        for row in range(board.get_dim()):
            if winner == provided.DRAW:
                scores[row][col] += 0

            elif winner == player and board.square(row, col) == player:
                scores[row][col] += SCORE_CURRENT
            elif winner == player and board.square(row, col) != player and board.square(row, col) != provided.EMPTY:
                scores[row][col] -= SCORE_OTHER
            elif winner != player and board.square(row, col) == player:
                scores[row][col] -= SCORE_CURRENT
            elif winner != player and board.square(row, col) != player and board.square(row, col) != provided.EMPTY:
                scores[row][col] += SCORE_OTHER
            elif board.square(row, col) == provided.EMPTY:
                scores[row][col] -= 0.0


def get_best_move(board, scores):
    """
    This function takes a current board and a grid of scores. The function
    should find all of the empty squares with the maximum score and randomly return
    one of them as a (row, column) tuple. It is an error to call this function
    with a board that has no empty squares (there is no possible next move), so
    your function may do whatever it wants in that case. The case where the board
    is full will not be tested.
    """

    max_score = -1000

    for col in range(board.get_dim()):
        for row in range(board.get_dim()):
            if scores[row][col] > max_score and board.square(row, col) == provided.EMPTY:
                max_score = scores[row][col]

    # find empty squares with max score
    empty_squares = board.get_empty_squares()
    candidate_move_list = []
    for square in empty_squares:
        if scores[square[0]][square[1]] == max_score:
            candidate_move_list.append(square)

    row, col = candidate_move_list[random.randrange(0, len(candidate_move_list))]
    return row, col


def mc_move(board, player, trials):
    """
    This function takes a current board, which player the machine player is,
    and the number of trials to run. The function should use the Monte Carlo simulation
    described above to return a move for the machine player in the form of a (row, column) tuple.
    Be sure to use the other functions you have written!
    """

    score_board = [[0 for dummy_col in range(board.get_dim())] for dummy_row in range(board.get_dim())]
    for dummy_i in range(trials):
        trial_board = board.clone()
        mc_trial(trial_board, player)
        mc_update_scores(score_board, trial_board, player)

    row, col = get_best_move(board, score_board)

    return row, col
