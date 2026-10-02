# Week 1 — Representing Problems

## Purpose

In AI, before we solve a problem, we must **define it**.

This week, we are not writing search algorithms. Instead, we are
learning how to represent a problem in a way that a computer can
understand.

The key idea is that AI works by exploring a **state space**.

## Core Concepts

### State

A representation of "where we are".

For our grid world, a state is represented as:

    (x, y)

### Actions

What we can do from a state.

For example:

- move up,
- move down,
- move left,
- move right.

### Transition

What happens when we perform an action.

## Tasks

1. Represent a grid world.
2. Define a function that returns valid neighbouring states.
3. Explore the state space.
4. Consider boundaries and edge cases.

## Reflection

- What exactly is a state?
- What makes a move valid or invalid?
- Why is defining the problem important before solving it?