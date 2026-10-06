"""
TU850-3
AINL3001 — Knowledge-Driven AI
Dr. Bianca Schoen-Phelan
2026

Week 4 Tutorial
Introducing the Problem Class

In previous weeks, we represented problems directly using
variables and functions.

From this week onwards, we will use a common Problem class
where appropriate.

This tutorial uses the familiar grid world from earlier weeks
to explore the new structure.
"""

from common.problem import Problem


GRID_SIZE = 5


class GridProblem(Problem):
    """
    A simple grid-world problem.

    A state is represented as an (x, y) coordinate.

    Example:

        (0, 0) = top-left corner
        (4, 4) = bottom-right corner
    """

    def actions(self, state):
        """
        Return the valid actions from this state.

        Possible actions:

            UP
            DOWN
            LEFT
            RIGHT

        Remember: an action must not move outside the grid.
        """

        # TODO:
        x, y = state
        actions = []

        # move up
        if y > 0:
            actions.append("up")

        # move down
        if y < GRID_SIZE - 1:
            actions.append("down")

        # move left
        if x > 0:
            actions.append("left")

        # move right
        if x < GRID_SIZE - 1:
            actions.append("right")

        return actions

    def result(self, state, action):
        """
        Return the new state produced by performing an action.

        Example:

            state  = (0, 0)
            action = "RIGHT"

            result = (1, 0)
        """

        # TODO:
        x,y = state

        # up move
        if action == "up":
            return(x,y -1)

        # down move
        if action == "down":
            return(x,y +1)

        # left move
        if action == "left":
            return(x -1, y)

        if action == "right":
            return(x +1, y)

        raise ValueError(f"ERROR action: {action}")


# --------------------------------------------------
# CREATE A PROBLEM
# --------------------------------------------------

problem = GridProblem(
    initial=(0, 0),
    goal=(4, 4)
)


# --------------------------------------------------
# EXPLORE THE PROBLEM
# --------------------------------------------------

print("Initial state:", problem.initial)
print("Goal:", problem.goal)


print("\nActions from (0, 0):")

actions = problem.actions((0, 0))

print(actions)


print("\nResults of those actions:")

if actions is not None:
    for action in actions:

        new_state = problem.result(
            (0, 0),
            action
        )

        print(
            action,
            "->",
            new_state
        )


print("\nIs (4, 4) the goal?")

print(
    problem.goal_test((4, 4))
)


# --------------------------------------------------
# REFLECTION QUESTIONS
# --------------------------------------------------

"""
Be ready to discuss:

1. What information is stored in problem.initial?
the start state (0,0)

2. What information is stored in problem.goal?
the goal state (4,4)

3. What is the difference between:

       problem.actions(state)

   and:

       problem.result(state, action)

       problem.action(state) returns all avaible actions from current state
       problem.result(state,action) returns the new current state after doing the action

4. Why doesn't Problem know anything about grids?
because problem is genric class for any problem not just grid.

5. Why doesn't GridProblem know anything about search?
because it is a specific problem which is not related to search algorithms, defies problem structure and rules not solution.

6. Could the same Problem structure be used for something
   other than a grid?
   yes, it is generic class, used for any problem with start and goal state and actions and results
"""