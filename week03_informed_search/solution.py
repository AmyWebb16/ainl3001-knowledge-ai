"""
AINL3001
BSP 2026
Topic 3 - Informed Search and Heuristics
Solution

Informed Search and Heuristics

This implementation includes:
- Manual heuristic exploration,
- Manhattan Distance,
- Greedy Best-First Search,
- A* Search,
- Comparison of algorithms.
"""

import heapq
from collections import deque


# --------------------------------------------------
# GRID CONFIGURATION
# --------------------------------------------------

GRID_SIZE = 10

START_STATE = (0, 0)

GOAL_STATE = (9, 9)

OBSTACLES = [
    (2, 1),
    (2, 2),
    (2, 3),
    (2, 4),
    (5, 6),
    (6, 6),
    (7, 6)
]


# --------------------------------------------------
# NEIGHBOURS
# --------------------------------------------------

def get_neighbours(state):

    x, y = state

    possible_moves = [
        (x + 1, y),
        (x - 1, y),
        (x, y + 1),
        (x, y - 1)
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
# MANHATTAN DISTANCE
# --------------------------------------------------

def manhattan_distance(state, goal):

    return (
        abs(goal[0] - state[0])
        +
        abs(goal[1] - state[1])
    )


# --------------------------------------------------
# PATH RECONSTRUCTION
# --------------------------------------------------

def reconstruct_path(parents, goal):

    path = []

    current = goal

    while current is not None:

        path.append(current)

        current = parents[current]

    return list(reversed(path))


# --------------------------------------------------
# BREADTH-FIRST SEARCH
# --------------------------------------------------
def breadth_first_search(start, goal):

    frontier = deque([start])

    visited = {start}

    parents = {
        start: None
    }

    # Nodes discovered during the search
    explored = [start]

    # Nodes removed from the frontier and processed
    expanded = []

    while frontier:

        current = frontier.popleft()

        expanded.append(current)

        if current == goal:

            path = reconstruct_path(
                parents,
                goal
            )

            return path, explored, expanded

        for neighbour in get_neighbours(current):

            if neighbour not in visited:

                visited.add(neighbour)

                explored.append(neighbour)

                parents[neighbour] = current

                frontier.append(neighbour)

    return [], explored, expanded

# --------------------------------------------------
# GREEDY BEST-FIRST SEARCH
# --------------------------------------------------
def greedy_best_first_search(start, goal):

    frontier = []

    heapq.heappush(
        frontier,
        (
            manhattan_distance(start, goal),
            start
        )
    )

    visited = {start}

    parents = {
        start: None
    }

    # Record nodes in the order they are discovered
    explored = [start]

    # Record nodes in the order they are expanded
    expanded = []

    while frontier:

        _, current = heapq.heappop(frontier)

        # This node has now been selected for expansion
        expanded.append(current)

        if current == goal:

            path = reconstruct_path(
                parents,
                goal
            )

            return path, explored, expanded

        for neighbour in get_neighbours(current):

            if neighbour not in visited:

                visited.add(neighbour)

                # Node has been discovered
                explored.append(neighbour)

                parents[neighbour] = current

                priority = manhattan_distance(
                    neighbour,
                    goal
                )

                heapq.heappush(
                    frontier,
                    (
                        priority,
                        neighbour
                    )
                )

    return [], explored, expanded


# --------------------------------------------------
# A*
# --------------------------------------------------
def astar(start, goal):

    frontier = []

    heapq.heappush(
        frontier,
        (
            manhattan_distance(start, goal),
            start
        )
    )

    parents = {
        start: None
    }

    cost_so_far = {
        start: 0
    }

    explored = [start]
    explored_set = {start}

    expanded = []

    while frontier:

        _, current = heapq.heappop(frontier)

        expanded.append(current)

        if current == goal:

            path = reconstruct_path(
                parents,
                goal
            )

            return path, explored, expanded

        for neighbour in get_neighbours(current):

            new_cost = (
                cost_so_far[current]
                + 1
            )

            if (
                neighbour not in cost_so_far
                or
                new_cost < cost_so_far[neighbour]
            ):

                cost_so_far[neighbour] = new_cost

                parents[neighbour] = current

                priority = (
                    new_cost
                    +
                    manhattan_distance(
                        neighbour,
                        goal
                    )
                )

                heapq.heappush(
                    frontier,
                    (
                        priority,
                        neighbour
                    )
                )

                if neighbour not in explored_set:

                    explored.append(neighbour)
                    explored_set.add(neighbour)

    return [], explored, expanded


# --------------------------------------------------
# MAIN
# --------------------------------------------------

# --------------------------------------------------
# MAIN
# --------------------------------------------------

# --------------------------------------------------
# MAIN
# --------------------------------------------------

if __name__ == "__main__":

    print("=" * 60)
    print("WEEK 3 - INFORMED SEARCH AND HEURISTICS")
    print("=" * 60)

    print(f"\nGrid Size: {GRID_SIZE} x {GRID_SIZE}")
    print(f"Start State: {START_STATE}")
    print(f"Goal State: {GOAL_STATE}")
    print(f"Obstacles: {OBSTACLES}")

    # ==================================================
    # TASK 0 - MANUAL HEURISTIC EXPLORATION
    # ==================================================

    print("\n" + "=" * 60)
    print("TASK 0 - MANUAL HEURISTIC EXPLORATION")
    print("=" * 60)

    states = {
        "State A": (0, 0),
        "State B": (2, 2),
        "State C": (4, 3)
    }

    distances = {}

    print(f"\nGoal State = {GOAL_STATE}")

    for name, state in states.items():

        distance = manhattan_distance(
            state,
            GOAL_STATE
        )

        distances[name] = distance

        print(f"\n{name} = {state}")
        print(f"Distance = {distance}")

    closest_state = min(
        distances,
        key=distances.get
    )

    furthest_state = max(
        distances,
        key=distances.get
    )

    print("\nRESULTS")

    print(
        f"Closest State: {closest_state}"
    )

    print(
        f"Furthest State: {furthest_state}"
    )

    print(
        "\nA heuristic estimates how close a state "
        "is to the goal."
    )

    print(
        "It can help a search algorithm prioritise "
        "more promising states."
    )

    # ==================================================
    # MANHATTAN DISTANCE EXAMPLES
    # ==================================================

    print("\n" + "=" * 60)
    print("MANHATTAN DISTANCE EXAMPLES")
    print("=" * 60)

    examples = [
        (0, 0),
        (2, 2),
        (5, 5),
        (8, 9)
    ]

    for state in examples:

        distance = manhattan_distance(
            state,
            GOAL_STATE
        )

        print(
            f"{state} -> {distance}"
        )

    # ==================================================
    # BREADTH-FIRST SEARCH
    # ==================================================

    print("\n" + "=" * 60)
    print("BREADTH-FIRST SEARCH")
    print("=" * 60)

    (
        bfs_path,
        bfs_explored,
        bfs_expanded
    ) = breadth_first_search(
        START_STATE,
        GOAL_STATE
    )

    print("\nFinal Path:")
    print(bfs_path)

    print("\nPath Length:")
    print(len(bfs_path) - 1)

    print("\nNodes Discovered:")
    print(bfs_explored)

    print("\nNumber of Nodes Discovered:")
    print(len(bfs_explored))

    print("\nNodes Expanded:")
    print(bfs_expanded)

    print("\nNumber of Nodes Expanded:")
    print(len(bfs_expanded))

    # ==================================================
    # GREEDY BEST-FIRST SEARCH
    # ==================================================

    print("\n" + "=" * 60)
    print("GREEDY BEST-FIRST SEARCH")
    print("=" * 60)

    (
        greedy_path,
        greedy_explored,
        greedy_expanded
    ) = greedy_best_first_search(
        START_STATE,
        GOAL_STATE
    )

    print("\nFinal Path:")
    print(greedy_path)

    print("\nPath Length:")
    print(len(greedy_path) - 1)

    print("\nNodes Discovered:")
    print(greedy_explored)

    print("\nNumber of Nodes Discovered:")
    print(len(greedy_explored))

    print("\nNodes Expanded:")
    print(greedy_expanded)

    print("\nNumber of Nodes Expanded:")
    print(len(greedy_expanded))

    # ==================================================
    # A* SEARCH
    # ==================================================

    print("\n" + "=" * 60)
    print("A* SEARCH")
    print("=" * 60)

    (
        astar_path,
        astar_explored,
        astar_expanded
    ) = astar(
        START_STATE,
        GOAL_STATE
    )

    print("\nFinal Path:")
    print(astar_path)

    print("\nPath Length:")
    print(len(astar_path) - 1)

    print("\nNodes Discovered:")
    print(astar_explored)

    print("\nNumber of Nodes Discovered:")
    print(len(astar_explored))

    print("\nNodes Expanded:")
    print(astar_expanded)

    print("\nNumber of Nodes Expanded:")
    print(len(astar_expanded))

    # ==================================================
    # SEARCH ALGORITHM COMPARISON
    # ==================================================

    print("\n" + "=" * 60)
    print("SEARCH ALGORITHM COMPARISON")
    print("=" * 60)

    print(
        f"\n{'Algorithm':<25}"
        f"{'Path':<12}"
        f"{'Discovered':<15}"
        f"{'Expanded':<12}"
    )

    print("-" * 64)

    print(
        f"{'Breadth-First Search':<25}"
        f"{len(bfs_path) - 1:<12}"
        f"{len(bfs_explored):<15}"
        f"{len(bfs_expanded):<12}"
    )

    print(
        f"{'Greedy Best-First':<25}"
        f"{len(greedy_path) - 1:<12}"
        f"{len(greedy_explored):<15}"
        f"{len(greedy_expanded):<12}"
    )

    print(
        f"{'A* Search':<25}"
        f"{len(astar_path) - 1:<12}"
        f"{len(astar_explored):<15}"
        f"{len(astar_expanded):<12}"
    )

    # ==================================================
    # FINAL PATH COMPARISON
    # ==================================================

    print("\n" + "=" * 60)
    print("FINAL PATH COMPARISON")
    print("=" * 60)

    print("\nBFS Path:")
    print(bfs_path)

    print("\nGreedy Path:")
    print(greedy_path)

    print("\nA* Path:")
    print(astar_path)

    # ==================================================
    # DISCUSSION
    # ==================================================

    print("\n" + "=" * 60)
    print("DISCUSSION")
    print("=" * 60)

    print(
        "\nBREADTH-FIRST SEARCH"
    )

    print(
        "BFS does not use a heuristic."
    )

    print(
        "It explores the search space level by level."
    )

    print(
        "When every move has the same cost, "
        "BFS finds a shortest path."
    )

    print(
        "\nGREEDY BEST-FIRST SEARCH"
    )

    print(
        "Greedy uses only the heuristic:"
    )

    print(
        "f(n) = h(n)"
    )

    print(
        "It selects the node that appears "
        "closest to the goal."
    )

    print(
        "Greedy can expand relatively few nodes, "
        "but it does not guarantee the shortest path."
    )

    print(
        "\nA* SEARCH"
    )

    print(
        "A* combines the path cost and heuristic:"
    )

    print(
        "f(n) = g(n) + h(n)"
    )

    print(
        "where:"
    )

    print(
        "g(n) = actual cost from the start "
        "to the current node"
    )

    print(
        "h(n) = estimated cost from the current "
        "node to the goal"
    )

    print(
        "With an appropriate heuristic, A* can "
        "guarantee a shortest path."
    )

    # ==================================================
    # DISCOVERED VS EXPANDED
    # ==================================================

    print("\n" + "-" * 60)
    print("DISCOVERED VS EXPANDED")
    print("-" * 60)

    print(
        "\nDiscovered:"
    )

    print(
        "A node has been found and added "
        "to the frontier."
    )

    print(
        "\nExpanded:"
    )

    print(
        "A node has been removed from the frontier "
        "and processed."
    )

    print(
        "\nTherefore, a node can be discovered "
        "without ever being expanded."
    )

    # ==================================================
    # IMPORTANT OBSERVATION
    # ==================================================

    print("\n" + "-" * 60)
    print("IMPORTANT OBSERVATION")
    print("-" * 60)

    print(
        "\nDifferent search algorithms may find "
        "different paths with the same path length."
    )

    print(
        "This can happen when multiple shortest "
        "paths exist."
    )

    print(
        "The order in which nodes are generated "
        "and ties are resolved can determine "
        "which shortest path is returned."
    )

    print(
        "\nThe number of expanded nodes tells us "
        "how much search work was required."
    )

    print(
        "A shorter final path does not necessarily "
        "mean fewer nodes were expanded."
    )

    print("\n" + "=" * 60)
    print("END")
    print("=" * 60)