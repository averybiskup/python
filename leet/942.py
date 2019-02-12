def diStringMatch(self, S):
        A = []
        r = list(range(0, len(S) + 1))

        for i in S:
            if str(i) == "I":
                A.append(r.pop(0)) # If we need to increase, we have to get the smallest number so we have somewhere to go from
            else:
                A.append(r.pop()) # If we need to decrease, we must get the largest number
        A.append(r.pop()) # Getting the last number from the array so we complete the new array

        return(A)
        
