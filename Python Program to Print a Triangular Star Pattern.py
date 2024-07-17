Python Program to Print a Triangular Star Pattern


def print_triangular_star_pattern(rows):
    for i in range(1, rows + 1):
        print('*' * i)

# Example usage:
rows = 5
print_triangular_star_pattern(rows)
