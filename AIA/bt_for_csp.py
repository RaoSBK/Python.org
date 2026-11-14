
# Backtracking Search for CSP

# Variables
variables = ['A', 'B', 'C', 'D']

# Domains: Possible colours for each variable
domains = {
    'A': ['Red', 'Green', 'Blue'],
    'B': ['Red', 'Green', 'Blue'],
    'C': ['Red', 'Green', 'Blue'],
    'D': ['Red', 'Green', 'Blue']
}

# Constraints: Neighbouring regions
neighbours = {
    'A': ['B', 'C'],
    'B': ['A', 'C', 'D'],
    'C': ['A', 'B', 'D'],
    'D': ['B', 'C']
}


# Check whether a value satisfies constraints
def is_consistent(variable, value, assignment):

    for neighbour in neighbours[variable]:

        # Check already assigned neighbours
        if neighbour in assignment:

            if assignment[neighbour] == value:
                return False

    return True


# Backtracking algorithm
def backtracking_search(assignment):

    # Base condition: All variables assigned
    if len(assignment) == len(variables):
        return assignment

    # Select an unassigned variable
    for variable in variables:
        if variable not in assignment:
            break

    # Try every value in its domain
    for value in domains[variable]:

        # Check whether assignment is valid
        if is_consistent(variable, value, assignment):

            # Assign value
            assignment[variable] = value

            # Recursively solve remaining variables
            result = backtracking_search(assignment)

            # If solution found, return it
            if result is not None:
                return result

            # Backtrack: remove the assignment
            del assignment[variable]

    # No valid value found
    return None


# Main program
solution = backtracking_search({})

if solution:
    print("Solution Found:")
    for variable, value in solution.items():
        print(variable, ":", value)
else:
    print("No solution exists")
