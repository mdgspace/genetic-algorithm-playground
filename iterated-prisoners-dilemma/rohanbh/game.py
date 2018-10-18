

def payoff_matrix(move_a, move_b):
    """A payoff matrix gives the payoff of each player in the game."""
    if (move_a, move_b) == (0, 0):
        # Both cooperate
        return 3, 3
    elif (move_a, move_b) == (0, 1):
        # A cooperates, B defects
        return 0, 5
    elif (move_a, move_b) == (1, 0):
        # A defects, B cooperates
        return 5, 0
    else:
        # Both defect
        return 1, 1

def play_iterated_game(player_a, player_b):
    """An iterated game represents 100 matches between two strategies. At the end of
    the game, the function returns the average score of each strategy."""
    net_score_a = net_score_b = 0
    player_a.reset_history()
    player_b.reset_history()
    for i in range(100):
        move_a = player_a.move()
        move_b = player_b.move()
        score_a, score_b = payoff_matrix(move_a, move_b)
        net_score_a += score_a
        net_score_b += score_b
        player_a.update([move_a, move_b])
        player_b.update([move_b, move_a])
    return net_score_a / 100, net_score_b / 100

