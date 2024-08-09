import collections


class Permutation:
    def __init__(self, st0):
        self.results = st0

    def create_string(self, curr, reserve):
        if not any(reserve.values()):
            self.results.add(curr)
            return

        for key in reserve.keys():
            if reserve[key]>0:
                reserve[key] -= 1
                self.create_string(curr+key, reserve)
                reserve[key] += 1
        return self.results


if __name__ == '__main__':
    ob = Permutation(set())
    st = input()
    ans = ob.create_string("", collections.Counter(st))
    sorted_ans = sorted(ans)
    print(len(sorted_ans))
    print("\n".join(sorted_ans))

