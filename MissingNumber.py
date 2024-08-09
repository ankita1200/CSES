if __name__ == "__main__":
    n = int(input())
    nums = list(map(int, input().split()))
    s1 = (n * (n+1))//2
    print(s1-sum(nums))

