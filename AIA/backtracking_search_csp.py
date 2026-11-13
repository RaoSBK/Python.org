
# Backtracking Search for CSP (Map Colouring)

# Variables and their possible colours (Domains)
variables = ['A', 'B', 'C', 'D']

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


# Check whether assigning a colour is valid
def is_valid(variable, colour, assignment):

    for neighbour in neighbours[variable]:

        # Check if the neighbour is already coloured
        if neighbour in assignment:

            # Adjacent regions must have different colours
            if assignment[neighbour] == colour:
                return False

    return True


# Backtracking Search function
def backtracking_search(assignment):

    # If all variables are assigned, return solution
    if len(assignment) == len(variables):
        return assignment

    # Select an unassigned variable
    for variable in variables:
        if variable not in assignment:
            break

    # Try every colour in the variable's domain
    for colour in domains[variable]:

        # Check constraints
        if is_valid(variable, colour, assignment):

            # Assign the colour
            assignment[variable] = colour

            # Recursively solve the remaining CSP
            result = backtracking_search(assignment)

            # If solution is found, return it
            if result is not None:
                return result

            # Backtrack: remove the assignment
            del assignment[variable]

    # No valid assignment found
    return None


# Main program
solution = backtracking_search({})

if solution:
    print("Solution Found:")
    for variable, colour in solution.items():
        print(variable, ":", colour)
else:
    print("No solution exists")
