import random


def evaluate(solution, items):
    v = sum(items[i]['v'] for i, b in enumerate(solution) if b)
    w = sum(items[i]['w'] for i, b in enumerate(solution) if b)
    return v, w


def _flip(solution, i):
    neighbor = list(solution)
    neighbor[i] ^= 1
    return neighbor


def local_search_first_improvement(items, capacity, init_sol=None):
    """Accept the first neighbor that strictly improves value."""
    n = len(items)
    sol = init_sol if init_sol is not None else [0] * n
    val, _ = evaluate(sol, items)

    improved = True
    while improved:
        improved = False
        indices = list(range(n))
        random.shuffle(indices)
        for i in indices:
            neighbor = _flip(sol, i)
            nv, nw = evaluate(neighbor, items)
            if nw <= capacity and nv > val:
                sol, val = neighbor, nv
                improved = True
                break

    return val, sol


def local_search_best_improvement(items, capacity, init_sol=None):
    """Scan all neighbors, accept the best one per iteration."""
    n = len(items)
    sol = init_sol if init_sol is not None else [0] * n
    val, _ = evaluate(sol, items)

    improved = True
    while improved:
        improved = False
        best_sol, best_val = sol, val
        for i in range(n):
            neighbor = _flip(sol, i)
            nv, nw = evaluate(neighbor, items)
            if nw <= capacity and nv > best_val:
                best_sol, best_val = neighbor, nv
                improved = True
        sol, val = best_sol, best_val

    return val, sol
