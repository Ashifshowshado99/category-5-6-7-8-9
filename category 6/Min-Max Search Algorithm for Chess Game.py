def minimax(depth, is_max):
    if depth == 0:
        return 0

    if is_max:
        best = -999
        for move in [1, 2]:
            score = minimax(depth - 1, False)
            best = max(best, score)
        return best

    else:
        best = 999
        for move in [1, 2]:
            score = minimax(depth - 1, True)
            best = min(best, score)
        return best


result = minimax(3, True)

print("Best score:", result)
print("Min-Max Search completed")