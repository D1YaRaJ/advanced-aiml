import math

HUMAN, AI, EMPTY = 'X', 'O', ' '

def create_board(): return [[EMPTY]*3 for _ in range(3)]

def print_board(b):
    for r in b: print('| ' + ' | '.join(r) + ' |')

def winner(b):
    lines = b + list(zip(*b)) + [[b[i][i] for i in range(3)], [b[i][2-i] for i in range(3)]]
    for line in lines:
        if line.count(line[0]) == 3 and line[0] != EMPTY:
            return line[0]
    return 'Draw' if all(c != EMPTY for r in b for c in r) else None

def minimax(b, is_max):
    win = winner(b)
    if win: return {'X': -1, 'O': 1, 'Draw': 0}[win]
    best = -math.inf if is_max else math.inf
    for i in range(3):
        for j in range(3):
            if b[i][j] == EMPTY:
                b[i][j] = AI if is_max else HUMAN
                score = minimax(b, not is_max)
                b[i][j] = EMPTY
                best = max(best, score) if is_max else min(best, score)
    return best

def best_move(b):
    move, best = None, -math.inf
    for i in range(3):
        for j in range(3):
            if b[i][j] == EMPTY:
                b[i][j] = AI
                score = minimax(b, False)
                b[i][j] = EMPTY
                if score > best:
                    best, move = score, (i, j)
    return move

def play():
    b = create_board()
    print("Tic Tac Toe: You (X) vs AI (O)")
    while True:
        print_board(b)
        if (w := winner(b)):
            print(f"{'Draw' if w == 'Draw' else f'{w} wins!'}")
            break
        # Human move
        while True:
            try:
                r, c = map(int, input("Enter row and col (0-2): ").split())
                if b[r][c] == EMPTY: break
                print("Cell taken.")
            except: print("Invalid input.")
        b[r][c] = HUMAN
        if not winner(b):
            ai = best_move(b)
            if ai: b[ai[0]][ai[1]] = AI

if __name__ == "__main__":
    play()