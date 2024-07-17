40. Print the characters at even index and odd index

def even_odd_index_chars(string):
    even_index_chars = string[::2]
    odd_index_chars = string[1::2]
    return even_index_chars, odd_index_chars
