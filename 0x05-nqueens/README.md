# N Queens

# Backtracking
Backtracking is a problem-solving technique that involves exploring all potential solutions to a problem and backtracking when a solution cannot be completed. It is often implemented using recursion. The algorithm tries to build a solution incrementally, one piece at a time, and removes those solutions that fail to satisfy the constraints of the problem at any point.

## How Backtracking Works
- **Choose:** Select a starting point or an initial solution.
- **Explore:** Try to extend the current solution by adding a new element.
- **Check:** If the current solution is valid, continue to extend it.
- **Backtrack:** If the current solution is not valid or leads to a dead end, remove the  last element added and try another option.
- **Repeat:** Continue this process until all possible solutions are explored.

# N-Queens Problem

The problem of placing N non-attacking queens on an N×N chessboard 
refers to the well-known "N-Queens" puzzle in chess. The objective is
to position N queens on the board in such a way 
that no two queens threaten each other. This means that:

- No two queens can be in the same row.
- No two queens can be in the same column.
- No two queens can be on the same diagonal.
For example, for a 4×4 chessboard, you need to find a 
configuration where 4 queens are placed according to these rules.
The challenge becomes increasingly complex as N increases, with various 
algorithms and strategies developed to find solutions.
