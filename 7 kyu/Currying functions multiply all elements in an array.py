def multiply_all(arr):
    def multiply(multiplier):
        return [i * multiplier for i in arr]
    return multiply