from spellchecker import SpellChecker

def spell_check(words):
    spell = SpellChecker()

    # find those words that may be misspelled
    misspelled = spell.unknown(words)

    d = {}
    for word in misspelled:
        corrections = spell.correction(word)
        candidates  = spell.candidates(word)
        d[word]     = {'corrections': corrections, 'candidates': candidates}

    return d

print(spell_check(['testin', 'morningg']))
