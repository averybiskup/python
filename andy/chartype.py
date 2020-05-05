c = input('Enter character: ')

vowels = ['a', 'e', 'i', 'o', 'u', 'y']
alph = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

if c in vowels:
    print('This is a vowel.')
elif c in alph:
    print('This is not a vowel.')
elif c.isdecimal():
    print('This is a digit.')
else:
    print('This is not a vowel, letter, or a number.')
