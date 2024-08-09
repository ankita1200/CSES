def generate_gray_code(n):
    if n <= 0:
        return []
    if n == 1:
        return ["0", "1"]
    code1 = ["0", "1"]
    code2 = ["1", "0"]
    ncode = []
    stlen = 1

    while stlen < n:
        for val in code1:
            ncode.append("0"+val)
        for val in code2:
            ncode.append("1"+val)
        code1 = ncode
        code2 = ncode[::-1]
        stlen += 1
        ncode = []
    return code1


if __name__ == '__main__':
    n = int(input())
    ans = generate_gray_code(n)
    print("\n".join(ans))
