Python Program to Print a Rectangular Star Pattern


def print_rectangular_star_pattern(rows, columns):
    for i in range(rows):
        print('*' * columns)

# Example usage:
rows = 5
columns = 10
print_rectangular_star_pattern(rows, columns)
