def sortArrayByParity(self, A):
        l = []
        for i in A:
            if i % 2 == 0:
                l = [i] + l
            else:
                l.append(i)
        return l
