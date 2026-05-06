import random


def greedy_deterministic(dist, start=0):
    """Nearest-neighbor: always pick the closest unvisited city."""
    n = len(dist)
    unvisited = set(range(n))
    unvisited.remove(start)
    route = [start]
    while unvisited:
        curr = route[-1]
        nxt = min(unvisited, key=lambda c: dist[curr, c])
        route.append(nxt)
        unvisited.remove(nxt)
    return route


def greedy_nondeterministic(dist, k=3):
    """At each step, pick randomly from the k nearest unvisited cities."""
    n = len(dist)
    start = random.randrange(n)
    unvisited = set(range(n))
    unvisited.remove(start)
    route = [start]
    while unvisited:
        curr = route[-1]
        candidates = sorted(unvisited, key=lambda c: dist[curr, c])[:k]
        nxt = random.choice(candidates)
        route.append(nxt)
        unvisited.remove(nxt)
    return route
