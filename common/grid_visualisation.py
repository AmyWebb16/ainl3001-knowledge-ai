"""
AINL3001 — Knowledge-Driven AI
BSP 2026

Grid Visualisation Utilities

This module provides simple grid-world visualisations used by
search algorithms throughout AINL3001.

The visualisation can show:

    - the start state,
    - the goal state,
    - obstacles,
    - the current state,
    - frontier states,
    - explored states,
    - the final solution path.

Colour Scheme
-------------

Light Green   Start State
Light Coral   Goal State
Black         Obstacles
Light Blue    Frontier
Light Grey    Explored States
Gold          Final Path

Example
-------

    from common.grid_visualisation import draw_grid

    draw_grid(
        grid_size=5,
        start=(0, 0),
        goal=(4, 4),
        current=(2, 2)
    )
"""

import matplotlib.pyplot as plt


def draw_grid(
    grid_size,
    start,
    goal,
    current=None,
    frontier=None,
    explored=None,
    path=None,
    obstacles=None,
    title="Grid World"
):
    """
    Draw a grid showing the current state of a search process.

    Parameters
    ----------
    grid_size : int
        Width and height of the square grid.

    start : tuple
        Starting state represented as (x, y).

    goal : tuple
        Goal state represented as (x, y).

    current : tuple, optional
        State currently being explored.

    frontier : list, optional
        States waiting to be explored.

    explored : list, optional
        States that have already been explored.

    path : list, optional
        States forming the final solution path.

    obstacles : list, optional
        Cells that cannot be entered.

    title : str, optional
        Title displayed above the grid.
    """

    # Use empty lists when optional values are not supplied.
    if frontier is None:
        frontier = []

    if explored is None:
        explored = []

    if path is None:
        path = []

    if obstacles is None:
        obstacles = []

    # Clear the current figure.
    plt.clf()

    ax = plt.gca()

    # --------------------------------------------------
    # Draw grid cells
    # --------------------------------------------------

    for y in range(grid_size):

        for x in range(grid_size):

            state = (x, y)

            # Default cell colour.
            colour = "white"

            # The order here determines which colours take priority.
            if state in explored:
                colour = "lightgrey"

            if state in frontier:
                colour = "lightskyblue"

            if state in path:
                colour = "gold"

            if state in obstacles:
                colour = "black"

            if state == start:
                colour = "lightgreen"

            if state == goal:
                colour = "lightcoral"

            square = plt.Rectangle(
                (x, y),
                1,
                1,
                facecolor=colour,
                edgecolor="black"
            )

            ax.add_patch(square)

    # --------------------------------------------------
    # Mark the current state
    # --------------------------------------------------

    if current is not None:

        plt.text(
            current[0] + 0.5,
            current[1] + 0.5,
            "X",
            ha="center",
            va="center",
            fontsize=12,
            fontweight="bold"
        )

    # --------------------------------------------------
    # Format the axes
    # --------------------------------------------------

    ax.set_xlim(0, grid_size)
    ax.set_ylim(0, grid_size)

    ax.set_xticks(range(grid_size))
    ax.set_yticks(range(grid_size))

    # Grid coordinates use (0, 0) as the top-left corner.
    ax.invert_yaxis()

    ax.set_aspect("equal")
    ax.set_title(title)

    # Set a useful title for the matplotlib window where supported.
    try:
        plt.gcf().canvas.manager.set_window_title(
            "AINL3001 Grid Visualisation"
        )
    except AttributeError:
        pass

    # Brief pause allows matplotlib to update during search.
    plt.pause(0.25)


def show_final_path(
    grid_size,
    start,
    goal,
    path,
    obstacles=None
):
    """
    Display the final path returned by a search algorithm.

    Parameters
    ----------
    grid_size : int
        Width and height of the square grid.

    start : tuple
        Starting state.

    goal : tuple
        Goal state.

    path : list
        States forming the final solution path.

    obstacles : list, optional
        Cells that cannot be entered.
    """

    if obstacles is None:
        obstacles = []

    plt.figure(figsize=(6, 6))

    draw_grid(
        grid_size=grid_size,
        start=start,
        goal=goal,
        path=path,
        obstacles=obstacles,
        title=f"Final Path (Length = {len(path)})"
    )

    plt.show()


def display_legend():
    """
    Print the colour meanings used by the grid visualisation.
    """

    print("\nVISUALISATION LEGEND")
    print("--------------------")
    print("Light Green = Start State")
    print("Light Coral = Goal State")
    print("Black       = Obstacle")
    print("Light Blue  = Frontier")
    print("Light Grey  = Explored")
    print("Gold        = Final Path")
    print()
