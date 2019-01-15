def numJewelsInStones(self, J, S):
        count = 0
        l = list(J)
        for i in S:
            if i in l:
                count += 1

        return count
