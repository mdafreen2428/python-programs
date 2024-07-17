11. Basic right triangle number pattern (inverted)


def inverted_right_triangle_number_pattern(n):
    for i in range(n, 0, -1):
        for j in range(1, i + 1):
            print(j, end=' ')
        print()
