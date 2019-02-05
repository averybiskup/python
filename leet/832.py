def flipAndInvertImage(self, A):
        A = map(lambda a: list(map(lambda b: 1 if b == 0 else 0, a))[::-1], A)
        return A
