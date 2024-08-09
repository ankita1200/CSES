def get_sets(n):
    i = 0 if n%2 != 0 else 1
    s = n if n%2 !=0 else n+1
    set1 = []
    set2 = []
    turn=1
    while i <= n//2:
        if turn:
            if i != 0:
                set1.append(i)
            set1.append(s-i)
            turn=0
        else:
            set2.append(i)
            set2.append(s-i)
            turn = 1
        i+=1
    return set1, set2


if __name__ == "__main__":
    n = int(input())
    if not (n * (n + 1) % 4 == 0):
        print("NO")
    else:
        print("YES")
        s1, s2 = get_sets(n)
        print(len(s1))
        print(" ".join(map(str, s1)))
        print(len(s2))
        print(" ".join(map(str, s2)))
