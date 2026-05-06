from load_tsp import tour_length


def _two_opt(route, i, j):
    return route[:i] + route[i:j + 1][::-1] + route[j + 1:]


def local_search_first_improvement(dist, route):
    """2-opt: accept the first swap that reduces tour length."""
    n = len(route)
    improved = True
    curr_len = tour_length(route, dist)
    while improved:
        improved = False
        for i in range(n - 1):
            for j in range(i + 2, n):
                neighbor = _two_opt(route, i, j)
                nl = tour_length(neighbor, dist)
                if nl < curr_len - 1e-10:
                    route, curr_len = neighbor, nl
                    improved = True
                    break
            if improved:
                break
    return route


def local_search_best_improvement(dist, route):
    """2-opt: scan all swaps, accept the best one per iteration."""
    n = len(route)
    improved = True
    while improved:
        improved = False
        best_len = tour_length(route, dist)
        best_route = route
        for i in range(n - 1):
            for j in range(i + 2, n):
                neighbor = _two_opt(route, i, j)
                nl = tour_length(neighbor, dist)
                if nl < best_len - 1e-10:
                    best_route, best_len = neighbor, nl
                    improved = True
        route = best_route
    return route
