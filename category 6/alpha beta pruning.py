def alphabeta(depth, alpha, beta, is_max):
    if depth == 0:
        return 0

    if is_max:
        best = -999
        for move in [1, 2]:
            score = alphabeta(depth - 1, alpha, beta, False)
            best = max(best, score)
            alpha = max(alpha, best)

            if beta <= alpha:
                break

        return best

    else:
        best = 999
        for move in [1, 2]:
            score = alphabeta(depth - 1, alpha, beta, True)
            best = min(best, score)
            beta = min(beta, best)

            if beta <= alpha:
                break

        return best


result = alphabeta(3, -999, 999, True)

print("Best score:", result)
print("Alpha-Beta Pruning completed")