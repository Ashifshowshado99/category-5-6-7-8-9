
# Map Coloring using CSP and Backtracking

# Define regions and their neighboring regions
graph = {
    'A': ['B', 'C'],
    'B': ['A', 'C', 'D'],
    'C': ['A', 'B', 'D'],
    'D': ['B', 'C']
}

# Available colors
colors = ['Red', 'Green', 'Blue']

# Store color assignments
assignment = {}


# Check whether a color is valid
def is_valid(region, color):
    for neighbor in graph[region]:
        if neighbor in assignment and assignment[neighbor] == color:
            return False
    return True


# Backtracking algorithm
def map_coloring(regions):
    if not regions:
        return True

    region = regions[0]

    for color in colors:
        if is_valid(region, color):
            assignment[region] = color

            if map_coloring(regions[1:]):
                return True

            # Backtrack
            del assignment[region]

    return False


# Main program
regions = list(graph.keys())

if map_coloring(regions):
    print("Map Coloring Solution:")
    for region, color in assignment.items():
        print(region, ":", color)
else:
    print("No solution exists")
