Python Program to Print a Half Diamond Star Pattern



def print_half_diamond(rows):
    # Upper part of the half diamond
    for i in range(1, rows + 1):
        print('*' * i)
    
    # Lower part of the half diamond
    for i in range(rows - 1, 0, -1):
        print('*' * i)

# Example usage:
rows = 5
print_half_diamond(rows)
