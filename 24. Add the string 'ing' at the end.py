24. Add the string 'ing' at the end of the given string if the length is more than 3. If the given string already exists then add 'ly'



def add_ing_ly(string):
    if len(string) > 3:
        if string.endswith('ing'):
            return string + 'ly'
        else:
            return string + 'ing'
    return string
