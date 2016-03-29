import random
from math import atan2

class GA:
    def individual(self, min, max):
        return random.uniform(min, max)

    def population(self, count, min, max):
        return [self.individual(min, max) for x in xrange(count)]

    def fitness(self, current_point, target_point, indiv):
        diffY = target_point['y'] - current_point['y']
        diffX = target_point['x'] - current_point['x']

        return abs(atan2(diffY, diffX) - indiv)

    def grade(self, current_point, target_point, popul):
        return sum([self.fitness(current_point, target_point, indiv) for indiv in popul]) / len(popul)

    def evolve(self, min, max, popul, current_point, target_point, retain=0.3, random_select=0.05, mutate=0.05):
        graded = [(self.fitness(current_point, target_point, indiv), indiv) for indiv in popul]

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

                child = self.individual(male, female)
                children.append(child)

        # MUTATE CHILDREN
        for i, indiv in enumerate(children):
            if mutate > random.random():
                children[i] = self.individual(min, max)

        return children