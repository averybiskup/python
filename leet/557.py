def reverseWords(s):
    l = list(map(lambda a: a[::-1], s.split()))
    return ' '.join(l)



print(reverseWords("s'teL ekat edoCteeL tsetnoc"))
