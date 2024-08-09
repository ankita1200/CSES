def combinations(no):
    if no <= 1:
        return str(0)
    result = [str(0)]
    for k in range(2, no+1):
        ans = int(((k**2 * (k**2-1))/2) - (4*(k-1)*(k-2)))
        result.append(str(ans))
    return result


if __name__ == "__main__":
    n = int(input())
    print("\n".join(combinations(n)))
