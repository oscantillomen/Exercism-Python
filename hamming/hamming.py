def distance(strand_a, strand_b):
    if len(strand_a) != len(strand_b):
        raise ValueError("Sequences have different lengths")
    distance = 0
    for index, letter in enumerate(strand_a):
        if strand_b[index] != letter:
            distance += 1
    return distance
