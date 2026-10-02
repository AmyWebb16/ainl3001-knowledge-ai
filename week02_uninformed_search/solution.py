"""
AINL3001 - Knowledge-Driven AI
BSP 2026
Topic 2 Solution

Uninformed Search

This solution demonstrates:

- Breadth-First Search (BFS),
- Depth-First Search (DFS),
- Path Reconstruction,
- BFS vs DFS Comparison,
- Final Path Visualisation.

"""

from collections import deque

from visualisation import show_final_path


# --------------------------------------------------
# GRID CONFIGURATION
# --------------------------------------------------

GRID_SIZE = 5

START_STATE = (0, 0)

GOAL_STATE = (4, 4)

OBSTACLES = [
    (1, 1),
    (2, 2),
    (3, 2)
]


# --------------------------------------------------
# NEIGHBOUR FUNCTION
# --------------------------------------------------

def get_neighbours(state):
    """
    Returns valid neighbouring states.

    A move is valid if:
    - it stays inside the grid
    - it does not move into an obstacle
    """

    x, y = state

    possible_moves = [
        (x + 1, y),  # right
        (x - 1, y),  # left
        (x, y + 1),  # down
        (x, y - 1)   # up
    ]

    neighbours = []

    for move in possible_moves:

        mx, my = move

        inside_grid = (
            0 <= mx < GRID_SIZE and
            0 <= my < GRID_SIZE
        )

        if inside_grid and move not in OBSTACLES:
            neighbours.append(move)

    return neighbours


# --------------------------------------------------
# PATH RECONSTRUCTION
# --------------------------------------------------

def reconstruct_path(parents, goal):
    """
    Reconstructs a path from goal
    back to start using the parents dictionary.
    """

    path = []

    current = goal

    while current is not None:
        path.append(current)
        current = parents[current]

    path.reverse()

    return path


# --------------------------------------------------
# BREADTH-FIRST SEARCH
# --------------------------------------------------

def bfs(start, goal):
    """
    Breadth-First Search

    Uses:
        Queue (FIFO)

    Returns:
        Path from start to goal
    """

    queue = deque([start])

    visited = {start}

    parents = {
        start: None
    }

    while queue:

        current = queue.popleft()

        if current == goal:
            return reconstruct_path(
                parents,
                goal
            )

        for neighbour in get_neighbours(current):

            if neighbour not in visited:

                visited.add(neighbour)

                parents[neighbour] = current

                queue.append(neighbour)

    return []


# --------------------------------------------------
# DEPTH-FIRST SEARCH
# --------------------------------------------------

def dfs(start, goal):
    """
    Depth-First Search

    Uses:
        Stack (Python list)

    Returns:
        Path from start to goal
    """

    stack = [start]

    visited = {start}

    parents = {
        start: None
    }

    while stack:

        current = stack.pop()

        if current == goal:
            return reconstruct_path(
                parents,
                goal
            )

        for neighbour in get_neighbours(current):

            if neighbour not in visited:

                visited.add(neighbour)

                parents[neighbour] = current

                stack.append(neighbour)

    return []


# --------------------------------------------------
# DISPLAY RESULTS
# --------------------------------------------------

def display_path_information(name, path):

    print("\n" + "=" * 50)
    print(name)
    print("=" * 50)

    print("\nPath:")
    print(path)

    if path:
        print("\nPath Length:")
        print(len(path) - 1)
    else:
        print("\nNo path found.")


# --------------------------------------------------
# MAIN PROGRAM
# --------------------------------------------------

print("\n" + "=" * 50)
print("WEEK 2 - BFS AND DFS COMPARISON")
print("=" * 50)

# ------------------------------------------
# BFS
# ------------------------------------------

bfs_path = bfs(
    START_STATE,
    GOAL_STATE
)

display_path_information(
    "BREADTH-FIRST SEARCH",
    bfs_path
)

# Visualise BFS path
show_final_path(
    grid_size=GRID_SIZE,
    start=START_STATE,
    goal=GOAL_STATE,
    path=bfs_path,
    obstacles=OBSTACLES
)

# ------------------------------------------
# DFS
# ------------------------------------------

dfs_path = dfs(
    START_STATE,
    GOAL_STATE
)

display_path_information(
    "DEPTH-FIRST SEARCH",
    dfs_path
)

# Visualise DFS path
show_final_path(
    grid_size=GRID_SIZE,
    start=START_STATE,
    goal=GOAL_STATE,
    path=dfs_path,
    obstacles=OBSTACLES
)

# ------------------------------------------
# COMPARISON
# ------------------------------------------

print("\n" + "=" * 50)
print("COMPARISON")
print("=" * 50)

bfs_length = len(bfs_path) - 1
dfs_length = len(dfs_path) - 1

print(f"\nBFS Path Length: {bfs_length}")
print(f"DFS Path Length: {dfs_length}")

if bfs_length < dfs_length:

    print(
        "\nObservation: BFS found a shorter path."
    )

elif dfs_length < bfs_length:

    print(
        "\nObservation: DFS found a shorter path."
    )

else:

    print(
        "\nObservation: Both algorithms found paths of equal length."
    )

print("\nDiscussion Points:")

print("- BFS uses a queue (FIFO).")
print("- DFS uses a stack (LIFO).")
print("- BFS explores level-by-level.")
print("- DFS explores one branch deeply first.")
print("- BFS guarantees a shortest path in this grid.")
print("- DFS does not guarantee a shortest path.")

print("\nEnd of demonstration.")