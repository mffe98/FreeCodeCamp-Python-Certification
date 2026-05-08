def fibonacci(n):
    if n < 0:
        raise ValueError('n must be positive')

    sequence = [0, 1]
    for step in range(n):
        sequence.append(sequence[step] + sequence[step + 1])
    return sequence[n]