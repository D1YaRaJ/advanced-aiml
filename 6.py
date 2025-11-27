import random
import math

# Fitness function (to be maximized)
def fitness(x):
    return x **2

# Initialize a population of 6 random values between 0 and 1
population = [random.uniform(0, 1) for _ in range(6)]
generations = 6  # total generations

# Mutation function (small random change)
def mutate(x):
    if random.random() < 0.3:        # 30% mutation chance
        x += random.uniform(-0.1, 0.1)
    return min(max(x, 0), 1)         # keep within range [0,1]

# Main evolution loop
for gen in range(generations):
    scores = [fitness(x) for x in population]  # evaluate fitness
    parents = sorted(zip(population, scores),key=lambda x: x[1], reverse=True)[:2]   #select top 2 parents
    p1, p2 = parents[0][0], parents[1][0]      # extract parent values

    # Crossover: create two children
    child1 = (p1 + p2) / 2                     # average
    child2 = (p1 * 0.75 + p2 * 0.25)           # weighted average

    # Apply mutation
    child1 = mutate(child1)
    child2 = mutate(child2)

    # New population: parents + children + random individuals
    population = [p1, p2, child1, child2] + [random.uniform(0, 1) for _ in range(2)]

    # Display generation info
    c=max(population,key=fitness)
    print(f"Generation {gen+1}: Population = {[round(x,3) for x in population]}, Best = {round(c,3)}, Fitness = {round(fitness(c),3)}")

# Find best individual
best = max(population, key=fitness)
print("\nBest Solution Found:", round(best, 3), "| Fitness =", round(fitness(best), 3))
