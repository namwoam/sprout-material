def drawSquare(size=3):
    if size < 3:
        return
    for i in range(size):
        if i == 0 or i == size - 1:
            print("="*size)
        else:
            print("="+" "*(size-2)+"=")
