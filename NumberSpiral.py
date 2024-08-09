def getvalue(x, y):
    if x == y:
        return 1 + y*(y-1)
    if x<y:
        diagonal = 1+y*(y-1)
        return diagonal+(y-x) if y % 2 != 0 else diagonal-(y-x)
    else:
        diagonal = 1 + x*(x-1)
        return diagonal+(x-y) if x % 2 == 0 else diagonal-(x-y)


if __name__ == '__main__':
    n = int(input())
    results = []
    for _ in range(n):
        row, col = map(int, input().split())
        results.append(str(getvalue(row, col)))
    print("\n".join(results))

