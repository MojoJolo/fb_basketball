import random
from math import atan2

def individual(min, max):
    return random.uniform(min, max)

def population(count, min, max):
    return [individual(min, max) for x in xrange(count)]

def fitness(current_point, target_point, indiv):
    diffY = target_point['y'] - current_point['y']
    diffX = target_point['x'] - current_point['x']

    return abs(atan2(diffY, diffX) - indiv)

def grade(current_point, target_point, popul):
    return sum([fitness(current_point, target_point, indiv) for indiv in popul]) / len(popul)

def evolve(min, max, popul, current_point, target_point, retain=0.2, random_select=0.05, mutate=0.1):
    graded = [(fitness(current_point, target_point, indiv), indiv) for indiv in popul]

    # SORT AND GET THE BEST PARENTS
    graded = [x[1] for x in sorted(graded)]
    retain_length = int(len(graded) * retain)
    parents = graded[:retain_length]

    # RANDOMLY SELECT ADDITIONAL PARENTS TO DIVERSIFY
    for indiv in graded[retain_length:]:
        if random_select > random.random():
            parents.append(indiv)

    # HAVE SEX. CROSSOVER
    parents_length = len(parents)
    desired_length = len(popul)

    children = []

    while len(children) < desired_length:
        male = random.randint(0, parents_length - 1)
        female = random.randint(0, parents_length - 1)

        if male != female:
            male = parents[male]
            female = parents[female]

            child = individual(male, female)
            children.append(child)

    # MUTATE CHILDREN
    for i, indiv in enumerate(children):
        if mutate > random.random():
            children[i] = individual(min, max)

    return children

min = -2.24
max = -0.76
population_count = 20

current_point = {
    'x': 187.5,
    'y': 530
}
target_point = {
    'x': 187.5,
    'y': 212
}

# print grade(current_point, target_point, population(population_count, min, max))

popul = population(population_count, min, max)
# print len(popul)

generations = [popul]

for i in xrange(10):
    popul = evolve(min, max, popul, current_point, target_point)
    generations.append(popul)
    # print len(popul)
    # print grade(current_point, target_point, popul)

best_indiv = [(fitness(current_point, target_point, indiv), indiv) for indiv in generations[-1]]
best_indiv = [x[1] for x in sorted(best_indiv)][0]

print best_indiv
