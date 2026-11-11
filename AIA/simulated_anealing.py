
import random
import math

# Objective function
def objective(x):
    return x ** 2


# Simulated Annealing algorithm
def simulated_annealing():

    # Initial solution
    current = random.uniform(-10, 10)

    # Initial temperature
    temperature = 100

    # Cooling rate
    cooling_rate = 0.95

    # Minimum temperature
    min_temperature = 0.01

    while temperature > min_temperature:

        # Generate a neighbouring solution
        neighbour = current + random.uniform(-1, 1)

        # Calculate change in cost
        delta = objective(neighbour) - objective(current)

        # Accept a better solution
        if delta < 0:
            current = neighbour

        # Sometimes accept a worse solution
        else:
            probability = math.exp(-delta / temperature)

            if random.random() < probability:
                current = neighbour

        # Reduce temperature
        temperature *= cooling_rate

    return current, objective(current)


# Run the algorithm
best_x, best_value = simulated_annealing()

print("Best solution:", best_x)
print("Minimum value:", best_value)
