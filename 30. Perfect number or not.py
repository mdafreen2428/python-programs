30. Perfect number or not



def is_perfect_number(num):
    return num == sum(i for i in range(1, num) if num % i == 0)
