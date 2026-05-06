import random
import math
from load_tsp import tour_length


def simulated_annealing(dist, temp=5000.0, cooling=0.995, iterations=5000):
    n = len(dist)
    route = list(range(n))
    random.shuffle(route)
    curr_len = tour_length(route, dist)
    best_route, best_len = list(route), curr_len

    for _ in range(iterations):
        i, j = sorted(random.sample(range(n), 2))
        neighbor = route[:i] + route[i:j + 1][::-1] + route[j + 1:]
        nl = tour_length(neighbor, dist)
        delta = nl - curr_len
        if delta < 0 or random.random() < math.exp(-delta / temp):
            route, curr_len = neighbor, nl
            if curr_len < best_len:
                best_route, best_len = list(route), curr_len
        temp *= cooling

    return best_route, best_len
