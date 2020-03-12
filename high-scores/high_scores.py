def latest(scores):
    return scores.pop()


def personal_best(scores):
    return max(scores)


def personal_top_three(scores):
    top_scores = []
    while (len(top_scores) < 3 and len(scores)):
        maxScore = max(scores)
        scores.remove(maxScore)
        top_scores.append(maxScore)
    return top_scores