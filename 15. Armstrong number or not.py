15. Armstrong number or not


def is_armstrong_number(num):
    digits = [int(d) for d in str(num)]
    power = len(digits)
    return num == sum(d ** power for d in digits)
