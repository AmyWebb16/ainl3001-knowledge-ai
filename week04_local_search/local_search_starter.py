"""
AINL3001 — Knowledge-Driven AI
Week 4 — Local Search and Optimisation
BSP 2026

This week introduces local search.

In previous weeks, search algorithms explored paths through
a state space in order to reach a goal.

Local search takes a different approach:

    1. Start with a state.
    2. Evaluate how good that state is.
    3. Generate neighbouring states.
    4. Move to a better neighbour.
    5. Repeat.

We will explore this using the N-Queens problem.

Tasks
-----

1. Understand the problem representation.
2. Implement conflict counting.
3. Explore neighbouring states.
4. Implement Hill Climbing.
5. Implement Simulated Annealing.
"""

import math
import random

from queens_problem import QueensProblem

N = 8


# --------------------------------------------------
# TASK 0 — UNDERSTANDING THE STATE
# --------------------------------------------------

example_board = [0, 1, 2, 3]

print("Manual Exploration Board:")
print(example_board)

print(
    "\nEach list position represents a column."
)

print(
    "Each value represents the row containing the queen."
)

print(
    "\nQuestion: How many conflicts exist on this board?"
)


# --------------------------------------------------
# TASK 1 — EVALUATE A STATE
# --------------------------------------------------

def count_conflicts(board):
    """
    Return the number of pairs of queens
    that attack each other.

    Lower values are better.

    A solution has:

        conflict count = 0
    """

    # TODO:
    conflicts = 0
    n = len(board)

    for col1 in range(n):
        row1 = board[col1]
        for col2 in range(col1 +1, n):
            row2 = board[col2]

            # check if queen same row
            if row1 == row2:
                conflicts = conflicts + 1

            # check if queens are diagonal
            if abs(row1 - row2) == abs(col1 - col2):
                conflicts = conflicts + 1

    return conflicts


# --------------------------------------------------
# TASK 2 — EXPLORE THE PROBLEM
# --------------------------------------------------

def generate_neighbours(problem, board):
    """
    Generate all neighbouring boards.

    Use the Problem interface introduced this week:

        problem.actions(state)
        problem.result(state, action)
    """

    neighbours = []

    # TODO:
    for action in problem.actions(board):
        new_state = problem.result(board, action)
        neighbours.append(new_state)
    return neighbours


# --------------------------------------------------
# TASK 3 — HILL CLIMBING
# --------------------------------------------------

def hill_climbing(problem, start_board):
    """
    Use Hill Climbing to reduce the number
    of conflicts.

    Algorithm:

        current = start state

        repeat:

            generate neighbours

            find the neighbour with the
            lowest conflict count

            if the neighbour is not better:
                stop

            otherwise:
                move to the neighbour

        return current
    """

    current = start_board

    # TODO
    while True:
            # make all neigbours of current board
            neighbours = generate_neighbours(problem,current)
    
            # find no. conflicts of each neighbour
            scored_neighbours = [(count_conflicts(board),board) for board in neighbours]

            # find neigbour with least conflicts
            best_score, best_board = min(scored_neighbours, key=lambda x: x[0])
    
            # see if best neighbour is correct
            current_score = count_conflicts(current)
    
            if best_score >= current_score:
                return current
    
            current = best_board


# --------------------------------------------------
# TASK 4 — SIMULATED ANNEALING
# --------------------------------------------------

def simulated_annealing(problem, start_board):
    """
    Use Simulated Annealing to search for
    a solution.

    Unlike Hill Climbing, Simulated Annealing
    can sometimes accept a worse state.

    This can help escape local minima.
    """

    current = start_board
    current_score = count_conflicts(current)

    temperature = 10.0
    cooling_rate = 0.95

    # TODO
    while temperature > 0.01:

        # get neighbours
        neighbours = generate_neighbours(problem, current)

        # pick random nighbour
        next_board = random.choice(neighbours)
        next_score = count_conflicts(next_board)

        # calcule cost of change
        delta = next_score - current_score

        # see if neighbour is better
        if delta< 0:
            current = next_board
            current_score = next_score

        else:
            prob = math.exp(-delta / temperature)
            if random.random() < prob:
                current = next_board
                current_score = next_score

        # cool temp
        temperature = temperature* cooling_rate

    return current


# --------------------------------------------------
# TESTING AREA
# --------------------------------------------------

if __name__ == "__main__":

    board = [
        random.randint(0, N - 1)
        for _ in range(N)
    ]

    problem = QueensProblem(board)

    print("\nRandom Board")
    print(board)

    print("\nConflicts")
    print(
        count_conflicts(board)
    )

    print("\nPossible Actions")

    actions = problem.actions(board)

    print(
        f"{len(actions)} actions available"
    )

    print("\nNeighbours")

    neighbours = generate_neighbours(
        problem,
        board
    )

    print(
        f"{len(neighbours)} neighbours generated"
    )

    print("\nHill Climbing")
    hill_board = hill_climbing(problem, board)
    print(hill_board)

    print("\nHill Conflicts")
    print(count_conflicts(hill_board))

    print("\nSimulated Annealing")
    sa_board = simulated_annealing(problem, board)
    print(sa_board)

    print("\nSimulated Annealing Conflicts")
    print(count_conflicts(sa_board))