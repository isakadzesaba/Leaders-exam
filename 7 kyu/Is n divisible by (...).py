def is_divisible(n, * arguments):
    return all(n % i == 0 for i in arguments) if arguments else True