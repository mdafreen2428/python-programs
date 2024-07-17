39. Changing the order of words in a string

def reverse_words(string):
    return ' '.join(string.split()[::-1])
