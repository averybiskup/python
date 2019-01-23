def uniqueMorseRepresentations(words):
        c = [".-","-...","-.-.","-..",".","..-.","--.","....","..",".---","-.-",".-..","--","-.","---",".--.","--.-",".-.","...","-","..-","...-",".--","-..-","-.--","--.."]
        d = {}

        for i in words:
            d["".join(list(map(lambda x: c[ord(x) - 97], list(i))))] = 1

        return len(d)

words = ["rwjje","aittjje","auyyn","lqtktn","lmjwn"]
print(uniqueMorseRepresentations(words))
