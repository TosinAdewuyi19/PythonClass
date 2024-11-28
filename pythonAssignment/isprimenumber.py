def isPrimeNumber(integer):
    if integer <= 1:
        return False
    for count in range(2, integer):
        if integer % count == 0:
            return False
    return True

