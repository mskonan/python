import random

# Parameters
POPULATION_SIZE = 6
GENES = 5  # Number of bits for representing a number (0-31)
GENERATIONS = 20
MUTATION_RATE = 0.1

# Fitness Function: f(x) = x^2
def fitness(individual):
    x = int("".join(map(str, individual)), 2)
    return x ** 2

# Create an individual
def create_individual():
    return [random.randint(0, 1) for _ in range(GENES)]

# Create the initial population
def create_population():
    return [create_individual() for _ in range(POPULATION_SIZE)]

# Select two parents from the population based on fitness (Roulette Wheel Selection)
def select_parents(population):
    total_fitness = sum(fitness(ind) for ind in population)
    wheel = [fitness(ind) / total_fitness for ind in population]
    
    def spin_wheel():
        pick = random.uniform(0, 1)
        current = 0
        for i, prob in enumerate(wheel):
            current += prob
            if current > pick:
                return population[i]
    
    return spin_wheel(), spin_wheel()

# Crossover between two parents
def crossover(parent1, parent2):
    crossover_point = random.randint(1, GENES - 1)
    return parent1[:crossover_point] + parent2[crossover_point:]

# Mutate an individual
def mutate(individual):
    return [gene if random.random() > MUTATION_RATE else 1 - gene for gene in individual]

# Main Genetic Algorithm Function
def genetic_algorithm():
    population = create_population()
    
    for generation in range(GENERATIONS):
        # Sort population by fitness
        population = sorted(population, key=fitness, reverse=True)
        print(f"Generation {generation + 1}: Best Individual = {population[0]}, Fitness = {fitness(population[0])}")

        # Create next generation
        new_population = []
        
        # Elitism: Preserve the best individual
        new_population.append(population[0])
        
        # Create rest of the new population
        while len(new_population) < POPULATION_SIZE:
            parent1, parent2 = select_parents(population)
            offspring = mutate(crossover(parent1, parent2))
            new_population.append(offspring)
        
        population = new_population

if __name__ == "__main__":
    genetic_algorithm()

