10. Basic right triangle number pattern


def right_triangle_number_pattern(n):
    for i in range(1, n + 1):
        for j in range(1, i + 1):
            print(j, end=' ')
        print()
