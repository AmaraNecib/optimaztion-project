import random
import math


def evaluate(solution, items):
    v = sum(items[i]['v'] for i, b in enumerate(solution) if b)
    w = sum(items[i]['w'] for i, b in enumerate(solution) if b)
    return v, w


def simulated_annealing(items, capacity, temp=1000.0, cooling=0.99, iterations=1000):
    n = len(items)
    sol = [0] * n
    val, _ = evaluate(sol, items)
    best_sol, best_val = list(sol), val

    for _ in range(iterations):
        i = random.randint(0, n - 1)
        neighbor = list(sol)
        neighbor[i] ^= 1
        nv, nw = evaluate(neighbor, items)

        if nw <= capacity:
            delta = nv - val
            if delta > 0 or random.random() < math.exp(delta / temp):
                sol, val = neighbor, nv
                if val > best_val:
                    best_sol, best_val = list(sol), val

        temp *= cooling

    return best_val, best_sol
