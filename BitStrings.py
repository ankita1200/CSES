def calculate_bit_strings(n):
    MOD = 10**9 + 7
    result = pow(2, n, MOD)
    return result


if __name__ == '__main__':
    n = int(input())
    print(calculate_bit_strings(n))


