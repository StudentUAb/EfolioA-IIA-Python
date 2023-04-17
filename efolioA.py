import time
from collections import deque
from copy import deepcopy

# contador de fronteiras
def count_borders(matrix):
    borders = 0
    n = len(matrix)
    m = len(matrix[0])

    for i in range(n):
        for j in range(m):
            if i > 0 and matrix[i][j] != matrix[i - 1][j]:
                borders += 1
            if j > 0 and matrix[i][j] != matrix[i][j - 1]:
                borders += 1

    return borders


# busca em profundidade
def dfs(matrix, max_borders):
    start_time = time.time()

    n = len(matrix)
    m = len(matrix[0])

    visited = set()
    stack = [(matrix, [])]

    generations = 0
    expansions = 0

    while stack:
        generations += 1
        current_matrix, actions = stack.pop()
        current_borders = count_borders(current_matrix)

        if current_borders <= max_borders:
            processing_time = time.time() - start_time
            return current_matrix, actions, current_borders, generations, expansions, processing_time

        for i in range(n):
            for j in range(m):
                for x, y in [(i - 1, j), (i + 1, j), (i, j - 1), (i, j + 1)]:
                    if 0 <= x < n and 0 <= y < m:
                        expansions += 1
                        new_matrix = deepcopy(current_matrix)
                        new_matrix[i][j], new_matrix[x][y] = new_matrix[x][y], new_matrix[i][j]

                        if tuple(map(tuple, new_matrix)) not in visited:
                            new_actions = actions + [((i, j), (x, y))]
                            stack.append((new_matrix, new_actions))
                            visited.add(tuple(map(tuple, new_matrix)))

        if time.time() - start_time > 60:
            break

    processing_time = time.time() - start_time
    return None, [], -1, generations, expansions, processing_time

def bfs(matrix, max_borders):
    start_time = time.time()

    n = len(matrix)
    m = len(matrix[0])

    visited = set()
    queue = deque([(matrix, [])])

    generations = 0
    expansions = 0

    while queue:
        generations += 1
        current_matrix, actions = queue.popleft()
        current_borders = count_borders(current_matrix)

        if current_borders <= max_borders:
            processing_time = time.time() - start_time
            return current_matrix, actions, current_borders, generations, expansions, processing_time

        for i in range(n):
            for j in range(m):
                for x, y in [(i - 1, j), (i + 1, j), (i, j - 1), (i, j + 1)]:
                    if 0 <= x < n and 0 <= y < m:
                        expansions += 1
                        new_matrix = deepcopy(current_matrix)
                        new_matrix[i][j], new_matrix[x][y] = new_matrix[x][y], new_matrix[i][j]

                        if tuple(map(tuple, new_matrix)) not in visited:
                            new_actions = actions + [((i, j), (x, y))]
                            queue.append((new_matrix, new_actions))
                            visited.add(tuple(map(tuple, new_matrix)))

        if time.time() - start_time > 60:
            break

    processing_time = time.time() - start_time
    return None, [], -1, generations, expansions, processing_time


def apply_action(matrix, action):
    new_matrix = deepcopy(matrix)
    (i, j), (x, y) = action
    new_matrix[i][j], new_matrix[x][y] = new_matrix[x][y], new_matrix[i][j]
    return new_matrix



instances = [
  [
        [1, 2, 3],
        [1, 2, 2],
        [3, 3, 1]
    ],
    [
        [1, 2, 2, 2],
        [1, 2, 1, 1]
    ],
    [
        [1, 2, 2, 2],
        [1, 3, 3, 3],
        [1, 2, 1, 1],
        [1, 1, 3, 2]
    ],
    [
        [1, 1, 2, 1, 1],
        [2, 2, 1, 2, 1],
        [1, 1, 2, 1, 2],
        [2, 1, 1, 2, 1]
    ],
    [
        [1, 2, 2, 2, 2, 1, 2, 2, 2, 2],
        [1, 3, 3, 3, 4, 1, 3, 3, 3, 4],
        [1, 2, 1, 4, 3, 1, 2, 1, 4, 3],
        [1, 4, 4, 4, 3, 1, 4, 4, 4, 3]
    ],
    [
        [1, 1, 2, 1, 1, 1, 1, 2, 1, 1],
        [2, 2, 1, 2, 1, 2, 2, 1, 2, 1],
        [1, 1, 2, 1, 2, 1, 1, 2, 1, 2],
        [2, 1, 1, 2, 1, 2, 1, 1, 2, 1],
        [1, 1, 2, 1, 1, 1, 1, 2, 1, 1],
        [2, 2, 1, 2, 1, 2, 2, 1, 2, 1],
        [1, 1, 2, 1, 2, 1, 1, 2, 1, 2],
        [2, 1, 1, 2, 1, 2, 1, 1, 2, 1]
    ],
    [
        [1, 1, 2, 8, 8, 1, 4, 3, 1, 4],
        [2, 2, 1, 8, 3, 8, 4, 3, 2, 1],
        [1, 1, 8, 8, 3, 1, 6, 2, 1, 4],
        [2, 1, 1, 3, 1, 2, 1, 1, 4, 4],
        [1, 7, 7, 3, 1, 1, 5, 6, 4, 4],
        [2, 2, 1, 3, 1, 2, 2, 1, 6, 6],
        [1, 7, 2, 7, 5, 5, 5, 5, 1, 6],
        [2, 7, 7, 7, 1, 5, 5, 1, 6, 6]
]

]

W1 = [6, 4, 10, 10, 30, 41, 70]

W2 = [5, 2, 9, 9, 25, 35, 62]

print("Selecione o método (DFS ou BFS):")
selected_method = input().strip().lower()

results = []

for idx, instance in enumerate(instances):
    if selected_method == 'dfs':
        result_matrix, actions, final_borders, generations, expansions, processing_time = dfs(instance, W1[idx]) #W1[idx] trocar por W2[idx] para usar W2
    elif selected_method == 'bfs':
        result_matrix, actions, final_borders, generations, expansions, processing_time = bfs(instance, W1[idx]) #W1[idx] trocar por W2[idx] para usar W2
    else:
        print("Método inválido.")
        break

    print(f"Instância {idx + 1}:")
    print(f"Fronteiras iniciais: {count_borders(instance)}")
    print(f"Número de gerações: {generations}")
    print(f"Número de expansões: {expansions}")
    print(f"Tempo de processamento: {processing_time:.2f} seconds")
    print()

    if final_borders == -1:
        print("Sem solução")
    else:
        print(f"Fronteiras finais: {final_borders}")

    print("\n")
