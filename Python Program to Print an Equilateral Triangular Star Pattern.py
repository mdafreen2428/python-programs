Python Program to Print an Equilateral Triangular Star Pattern

def print_equilateral_triangle(rows):
    for i in range(1, rows + 1):
        # Print leading spaces
        for j in range(rows - i):
            print(' ', end='')
        # Print stars
        for k in range(2 * i - 1):
            print('*', end='')
        # Move to the next line
        print()

# Example usage:
rows = 5
print_equilateral_triangle(rows)
