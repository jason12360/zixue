def search4vowels(word):
    """Return any vowels found in a supplied word."""
    vowels = set('aeiou')
    return vowels.intersection(set(word))


def search4letters(word,letters):
    """Return any letters found in a supplied word."""
    
    return set(word).intersection(set(letters))