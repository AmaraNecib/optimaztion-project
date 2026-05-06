import random
from load_tsp import tour_length


def _ox_crossover(p1, p2):
    """Ordered Crossover (OX): preserve relative order from both parents."""
    n = len(p1)
    a, b = sorted(random.sample(range(n), 2))
    child = [None] * n
    child[a:b] = p1[a:b]
    segment = set(child[a:b])
    fill = [c for c in p2 if c not in segment]
    ptr = 0
    for i in range(n):
        if child[i] is None:
            child[i] = fill[ptr]
            ptr += 1
    return child


def genetic_algorithm(dist, pop_size=100, generations=200, mutation_rate=0.1):
    n = len(dist)
    pop = [random.sample(range(n), n) for _ in range(pop_size)]

    for _ in range(generations):
        pop.sort(key=lambda r: tour_length(r, dist))
        elites = [list(r) for r in pop[:max(1, pop_size // 10)]]
        new_pop = elites[:]

        top = pop[:max(2, pop_size // 4)]
        while len(new_pop) < pop_size:
            p1, p2 = random.choices(top, k=2)
            child = _ox_crossover(p1, p2)
            if random.random() < mutation_rate:
                i, j = random.sample(range(n), 2)
                child[i], child[j] = child[j], child[i]
            new_pop.append(child)

        pop = new_pop

    best = min(pop, key=lambda r: tour_length(r, dist))
    return best, tour_length(best, dist)
