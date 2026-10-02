"""
TU850-3
AINL3001 — Knowledge-Driven AI
Dr. Bianca Schoen-Phelan
2026

Topic 1 Lab: Representing Problems
AINL3001 — Topic 1 Solution


It includes:
- Clear state representation,
- Fully working neighbour logic,
- Multiple test scenarios,
- Explicit demo outputs.

"""

# --------------------------------------------------
# STEP 1: Define the grid
# --------------------------------------------------

GRID_SIZE = 5

# Define a clear start state (explicitly included now)
START_STATE = (0, 0)

# Optional: define a goal (used later in module)
GOAL_STATE = (4, 4)


# --------------------------------------------------
# STEP 2: Define neighbours function
# --------------------------------------------------

def get_neighbours(state):
    """
    Returns valid neighbouring states for a given position.

    A state is a tuple: (x, y)

    Valid moves:
    - Up, Down, Left, Right

    We must ensure that no movement outside the grid.
    """

    x, y = state
    neighbours = []

    # MOVE UP
    if y > 0:
        neighbours.append((x, y - 1))

    # MOVE DOWN
    if y < GRID_SIZE - 1:
        neighbours.append((x, y + 1))

    # MOVE LEFT
    if x > 0:
        neighbours.append((x - 1, y))

    # MOVE RIGHT
    if x < GRID_SIZE - 1:
        neighbours.append((x + 1, y))

    return neighbours


# --------------------------------------------------
# DEMONSTRATION SCENARIOS
# --------------------------------------------------

print("====================================")
print(" WEEK 1 DEMONSTRATION")
print("====================================\n")

# Scenario 1: Starting position
print("Scenario 1: Start State")
print("----------------------")
print("State:", START_STATE)
print("Neighbours:", get_neighbours(START_STATE))
print()

# Scenario 2: Middle of grid
middle_state = (2, 2)

print("Scenario 2: Middle State")
print("------------------------")
print("State:", middle_state)
print("Neighbours:", get_neighbours(middle_state))
print()

# Scenario 3: Edge of grid
edge_state = (0, 3)

print("Scenario 3: Edge State")
print("----------------------")
print("State:", edge_state)
print("Neighbours:", get_neighbours(edge_state))
print()

# Scenario 4: Corner (opposite)
corner_state = (4, 4)

print("Scenario 4: Corner State")
print("------------------------")
print("State:", corner_state)
print("Neighbours:", get_neighbours(corner_state))
print()

# --------------------------------------------------
# SCENARIO 5: Explore multiple states automatically
# --------------------------------------------------

print("Scenario 5: Multiple State Exploration")
print("--------------------------------------")

test_states = [
    (0, 0),
    (1, 1),
    (2, 2),
    (4, 4),
]

for state in test_states:
    print(f"{state} -> {get_neighbours(state)}")

print()


# --------------------------------------------------
# OPTIONAL EXTENSION: OBSTACLES
# --------------------------------------------------

print("Scenario 6: With Obstacles")
print("--------------------------")

# Define blocked cells
OBSTACLES = [(1, 1), (2, 2)]

def get_neighbours_with_obstacles(state):
    neighbours = get_neighbours(state)

    # Remove blocked cells
    valid = [n for n in neighbours if n not in OBSTACLES]
    return valid

test_state = (1, 2)

print("State:", test_state)
print("Obstacles:", OBSTACLES)
print("Valid neighbours:", get_neighbours_with_obstacles(test_state))

# --------------------------------------------------
# VISUALISATION EXTENSION
# --------------------------------------------------

# V1 SIMPLE:
def display_grid(current=None, neighbours=None):
    """
    Prints a visual grid:
    S = start
    X = current state
    * = neighbours
    . = empty cell
    """

    for y in range(GRID_SIZE):
        row = []
        for x in range(GRID_SIZE):
            cell = (x, y)

            if cell == START_STATE:
                row.append("S")
            elif current and cell == current:
                row.append("X")
            elif neighbours and cell in neighbours:
                row.append("*")
            else:
                row.append(".")

        print(" ".join(row))
    print("\n")

state = (2, 2)
neigh = get_neighbours(state)

print("Visualising state and neighbours:\n")
display_grid(current=state, neighbours=neigh)

# V2 ENHANCED DISPLAY with COORDINATE AXIS

def display_grid_with_axes(current=None, neighbours=None):
    print("   " + " ".join(str(x) for x in range(GRID_SIZE)))

    for y in range(GRID_SIZE):
        row = []
        for x in range(GRID_SIZE):
            cell = (x, y)

            if cell == START_STATE:
                row.append("S")
            elif current and cell == current:
                row.append("X")
            elif neighbours and cell in neighbours:
                row.append("*")
            else:
                row.append(".")

        print(f"{y}  " + " ".join(row))
    print()
    

print("Visualising state and neighbours:\n")
display_grid_with_axes(current=state, neighbours=neigh)


# V3 matplotlib

import matplotlib.pyplot as plt

def plot_grid(current=None, neighbours=None):
    fig, ax = plt.subplots()

    # Set custom window title
    fig.canvas.manager.set_window_title("Grid World (Week 1 Demo)")

    # Draw grid lines
    for x in range(GRID_SIZE + 1):
        ax.axhline(x, linewidth=1)
        ax.axvline(x, linewidth=1)

    # Plot cells
    for y in range(GRID_SIZE):
        for x in range(GRID_SIZE):
            if (x, y) == START_STATE:
                ax.text(x + 0.5, y + 0.5, "S", ha='center', va='center')
            elif current and (x, y) == current:
                ax.text(x + 0.5, y + 0.5, "X", ha='center', va='center')
            elif neighbours and (x, y) in neighbours:
                ax.text(x + 0.5, y + 0.5, "*", ha='center', va='center')

    ax.set_xlim(0, GRID_SIZE)
    ax.set_ylim(0, GRID_SIZE)

    ax.invert_yaxis()
    ax.set_xticks(range(GRID_SIZE))
    ax.set_yticks(range(GRID_SIZE))

    plt.show()


plot_grid(current=state, neighbours=neigh)
