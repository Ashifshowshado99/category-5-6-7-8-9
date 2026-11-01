
# Local Search for CSP using Min-Conflicts

import random

# Define the graph
graph = {
    'A': ['B', 'C'],
    'B': ['A', 'C', 'D'],
    'C': ['A', 'B', 'D'],
    'D': ['B', 'C']
}

colors = ['Red', 'Green', 'Blue']


# Count conflicts for a variable
def count_conflicts(region, color, assignment):
    conflicts = 0

    for neighbor in graph[region]:
        if assignment[neighbor] == color:
            conflicts += 1

    return conflicts


# Find conflicted variables
def get_conflicted_variables(assignment):
    conflicted = []

    for region in graph:
        if count_conflicts(
            region, assignment[region], assignment
        ) > 0:
            conflicted.append(region)

    return conflicted


# Min-Conflicts algorithm
def min_conflicts(max_steps=1000):

    # Initial random assignment
    assignment = {
        region: random.choice(colors)
        for region in graph
    }

    for step in range(max_steps):

        conflicted = get_conflicted_variables(assignment)

        # Check whether solution is found
        if not conflicted:
            return assignment

        # Select a random conflicted variable
        region = random.choice(conflicted)

        # Find colors with minimum conflicts
        min_conflict = min(
            count_conflicts(region, color, assignment)
            for color in colors
        )

        best_colors = [
            color for color in colors
            if count_conflicts(region, color, assignment)
            == min_conflict
        ]

        # Assign the best color
        assignment[region] = random.choice(best_colors)

    return None


# Main program
random.seed(10)

solution = min_conflicts()

if solution:
    print("Solution Found using Min-Conflicts:")

    for region, color in solution.items():
        print(region, ":", color)

    print("\nAll constraints satisfied!")
else:
    print("Solution not found within maximum steps.")
