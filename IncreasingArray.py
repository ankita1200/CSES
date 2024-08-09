def get_increasing_array(arr):
    moves = 0
    for i in range(1, len(arr)):
        if arr[i] < arr[i-1]:
            moves += arr[i-1]-arr[i]
            arr[i] = arr[i-1]
    return moves


if __name__ == "__main__":
    n=int(input())
    arr = list(map(int, input().split()))
    print(get_increasing_array(arr))
