"""
TU850-3
AINL3001 — Knowledge-Driven AI
Dr. Bianca Schoen-Phelan
"""


class Problem:
    """
    Base class for problems explored by AI algorithms.

    A problem defines:
    - an initial state
    - a goal
    - the actions available from a state
    - the result of performing an action
    """

    def __init__(self, initial, goal):
        self.initial = initial
        self.goal = goal

    def actions(self, state):
        """Return the actions available from the given state."""
        raise NotImplementedError

    def result(self, state, action):
        """Return the state reached after performing an action."""
        raise NotImplementedError

    def goal_test(self, state):
        """Return True if the given state is a goal state."""
        return state == self.goal