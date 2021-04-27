def sum_numbers(*args):
    total = 0
    for a in args:
        total += a
    print(total)

sum_numbers(9, 73)
sum_numbers(4, 643, 654, 7565)
