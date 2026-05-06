import random


def evaluate(solution, items):
    v = sum(items[i]['v'] for i, b in enumerate(solution) if b)
    w = sum(items[i]['w'] for i, b in enumerate(solution) if b)
    return v, w


def greedy_deterministic(items, capacity):
    """Sort by value/weight ratio, greedily pick items."""
    order = sorted(range(len(items)), key=lambda i: items[i]['v'] / items[i]['w'], reverse=True)
    solution = [0] * len(items)
    total_w = total_v = 0
    for i in order:
        if total_w + items[i]['w'] <= capacity:
            solution[i] = 1
            total_w += items[i]['w']
            total_v += items[i]['v']
    return total_v, solution


def greedy_nondeterministic(items, capacity, k=5):
    """At each step, randomly pick from the top-k candidates by ratio."""
    order = sorted(range(len(items)), key=lambda i: items[i]['v'] / items[i]['w'], reverse=True)
    solution = [0] * len(items)
    total_w = total_v = 0
    remaining = list(order)
    while remaining:
        candidates = remaining[:k]
        i = random.choice(candidates)
        remaining.remove(i)
        if total_w + items[i]['w'] <= capacity:
            solution[i] = 1
            total_w += items[i]['w']
            total_v += items[i]['v']
    return total_v, solution
