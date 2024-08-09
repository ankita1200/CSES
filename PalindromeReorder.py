import collections


def rearrange(st):
    counts = collections.Counter(st)
    if len(counts) <= 1:
        return st
    even = {}
    odd={}
    for ch, count in counts.items():
        if count % 2 == 0:
            even[ch] = count
        else:
            odd[ch] = count
            if len(odd) > 1:
                return "NO SOLUTION"

    ans = list(odd.keys())[0] * list(odd.values())[0] if odd else ""
    for key, val in even.items():
        s = key * (val//2)
        ans = s + ans + s
    return ans


if __name__ == "__main__":
    st = input()
    print(rearrange(st))


