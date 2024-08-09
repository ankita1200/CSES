def hanoi(n, source, target, auxiliary, moves):
    if n == 1:
        moves.append((source, target))
        return
    hanoi(n - 1, source, auxiliary, target, moves)  # Move n-1 disks from source to auxiliary
    moves.append((source, target))  # Move the nth disk from source to target
    hanoi(n - 1, auxiliary, target, source, moves)  # Move n-1 disks from auxiliary to target


if __name__ == '__main__':
    n = int(input())
    moves = []
    hanoi(n, 1, 3, 2, moves)

    print(len(moves))  # Print the number of moves
    for move in moves:
        print(move[0], move[1])  # Print each move

