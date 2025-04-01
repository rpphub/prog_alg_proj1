import random

def generate_spiral_matrix(n):
    matrix = [[0] * n for _ in range(n)]
    numbers = [2, 3, 1]  # Meghatározott sorrend
    
    # Spirál koordináták
    directions = [(0, 1), (1, 0), (0, -1), (-1, 0)]  # Jobbra, le, balra, fel
    x, y, dir_index = 0, 0, 0
    path = []
    
    for _ in range(n * n):
        path.append((x, y))
        matrix[x][y] = -1  # Ideiglenesen foglalt hely
        
        # Következő pozíció
        new_x, new_y = x + directions[dir_index][0], y + directions[dir_index][1]
        
        # Ha kilépnénk a mátrixból vagy már foglalt helyre lépnénk, irányt váltunk
        if not (0 <= new_x < n and 0 <= new_y < n and matrix[new_x][new_y] == 0):
            dir_index = (dir_index + 1) % 4
            new_x, new_y = x + directions[dir_index][0], y + directions[dir_index][1]
        
        x, y = new_x, new_y
    
    # A számok elhelyezése soronként és oszloponként egyedileg a spirál mentén
    num_index = 0
    for row in range(n):
        available_positions = [pos for pos in path if pos[0] == row]
        random.shuffle(available_positions)
        for i, pos in enumerate(available_positions[:3]):
            x, y = pos
            matrix[x][y] = numbers[i % 3]
    
    # Az összes többi helyet 0-ra állítjuk
    for i in range(n):
        for j in range(n):
            if matrix[i][j] == -1:
                matrix[i][j] = 0
    
    return matrix


def print_matrix(matrix):
    for row in matrix:
        print(" ".join(map(str, row)))


n = 6
spiral_matrix = generate_spiral_matrix(n)
print_matrix(spiral_matrix)
