def number_pattern(n):
    if not isinstance(n, int):
        return 'Argument must be an integer value.'
    if n < 1:
        return 'Argument must be an integer greater than 0.'

    num_pattern = ''
    for num in range(1, n + 1):
        num_pattern += str(num)
        if num != n:
            num_pattern += ' '
    return num_pattern