
# Constraint Propagation in CSP

# Variables and their domains
domains = {
    'A': ['Red', 'Green', 'Blue'],
    'B': ['Red', 'Green', 'Blue'],
    'C': ['Red', 'Green', 'Blue']
}

# Neighbouring variables
neighbours = {
    'A': ['B'],
    'B': ['A', 'C'],
    'C': ['B']
}


# Check and remove inconsistent values
def revise(x, y):

    revised = False

    for value in domains[x][:]:

        # Check whether a compatible value exists in Y
        if not any(value != other for other in domains[y]):

            # Remove the invalid value
            domains[x].remove(value)
            revised = True

    return revised


# AC-3 Constraint Propagation
def constraint_propagation():

    # Create a queue of all arcs
    queue = []

    for x in neighbours:
        for y in neighbours[x]:
            queue.append((x, y))

    while queue:

        # Remove one arc from queue
        x, y = queue.pop(0)

        # Revise the domain of X
        if revise(x, y):

            # If domain becomes empty, no solution exists
            if len(domains[x]) == 0:
                return False

            # Add neighbouring arcs back to queue
            for z in neighbours[x]:

                if z != y:
                    queue.append((z, x))

    return True


# Main program
if constraint_propagation():

    print("Constraint Propagation Successful!")

    for variable in domains:
        print(variable, ":", domains[variable])

else:
    print("No solution exists")
