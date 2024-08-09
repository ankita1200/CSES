def possible_moves(a, b):
    check1 = (2*b-a)
    check2 = (2*a-b)
    if check1 % 3 == 0 and check2 % 3 == 0 and check1 >= 0 and check2 >= 0:
        return "YES"
    else:
        return "NO"


if __name__ == "__main__":
    n = int(input())
    ans = []
    for _ in range(n):
        a, b = map(int, input().split())
        ans.append(possible_moves(a, b))
    print("\n".join(ans))


