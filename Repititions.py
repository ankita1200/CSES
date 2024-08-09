def max_repetitions(st):
    maxval = 1
    count = 1
    for i in range(1, len(st)):
        if st[i] == st[i-1]:
            count += 1
        else:
            count = 1
        maxval = max(maxval, count)
    return maxval


if __name__ == "__main__":
    st = input()
    print(max_repetitions(st))


