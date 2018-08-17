"""Implement divmod function without using multiplication or division"""

def div_mod(a, b, log=False):
    result = 0
    cycles = 0
    while a >= b:
        times = 1
        base = b

        while (base << 1) < a:
            base <<= 1
            times <<= 1
            cycles += 1

        a -= base
        result += times

    if log:
        print('Cycles: {}'.format(cycles))

    return (result, a)


def main():
    a = 30
    b = 7
    result = div_mod(a, b)
    print(result)

    a = 45
    b = 9
    result = div_mod(a, b)
    print(result)

    a = 4
    b = 8
    result = div_mod(a, b)
    print(result)

    a = 18446744073709551616
    b = 2
    # Cycles: 1953, instead of 9223372036854775808 if we do this with sums
    result = div_mod(a, b, True)
    print(result)

if __name__ == '__main__':
    main()