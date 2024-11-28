def isSquare(integer):
    if integer < 0:
        return False
    root = int(integer ** 0.5)
    return root * root == integer

