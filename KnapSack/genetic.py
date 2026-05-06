import random


def fitness(solution, items, capacity):
    v = sum(items[i]['v'] for i, b in enumerate(solution) if b)
    w = sum(items[i]['w'] for i, b in enumerate(solution) if b)
    return v if w <= capacity else 0


def _crossover(p1, p2):
    cut = random.randint(1, len(p1) - 1)
    return p1[:cut] + p2[cut:]


def genetic_algorithm(items, capacity, pop_size=50, generations=100, mutation_rate=0.05):
    n = len(items)
    pop = [[random.randint(0, 1) for _ in range(n)] for _ in range(pop_size)]

    for _ in range(generations):
        pop.sort(key=lambda x: fitness(x, items, capacity), reverse=True)
        elites = [list(x) for x in pop[:max(1, pop_size // 10)]]
        new_pop = elites[:]

        top = pop[:max(2, pop_size // 4)]
        while len(new_pop) < pop_size:
            p1, p2 = random.choices(top, k=2)
            child = _crossover(p1, p2)
            if random.random() < mutation_rate:
                child[random.randint(0, n - 1)] ^= 1
            new_pop.append(child)

        pop = new_pop

    best = max(pop, key=lambda x: fitness(x, items, capacity))
    return fitness(best, items, capacity), best
