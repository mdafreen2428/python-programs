18. Finding factors of a number

def factors_of_number(num):
    return [i for i in range(1, num + 1) if num % i == 0]
