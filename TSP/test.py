import time
import sys
import numpy as np
from load_tsp import load_tsp, build_dist_matrix, tour_length
from greedy import greedy_deterministic, greedy_nondeterministic
from local_search import local_search_first_improvement, local_search_best_improvement
from simulated_annealing import simulated_annealing
from genetic import genetic_algorithm


def run(dist, label):
    print(f"\nTSP | {len(dist)} cities  ({label})")
    print(f"{'Algorithm':<35} {'Distance':>12} {'Time':>10}")
    print("-" * 60)

    greedy_route = greedy_deterministic(dist)

    tests = [
        ("Greedy Deterministic",
         lambda: (greedy_deterministic(dist), None)),
        ("Greedy Nondeterministic",
         lambda: (greedy_nondeterministic(dist), None)),
        ("Local Search First Improvement",
         lambda: (local_search_first_improvement(dist, list(greedy_route)), None)),
        ("Local Search Best Improvement",
         lambda: (local_search_best_improvement(dist, list(greedy_route)), None)),
        ("Simulated Annealing",
         lambda: simulated_annealing(dist)),
        ("Genetic Algorithm",
         lambda: genetic_algorithm(dist, pop_size=50, generations=100)),
    ]

    for name, fn in tests:
        t0 = time.perf_counter()
        result = fn()
        elapsed = time.perf_counter() - t0
        d = result[1] if result[1] is not None else tour_length(result[0], dist)
        print(f"{name:<35} {d:>12.2f} {elapsed:>9.4f}s")


if __name__ == "__main__":
    if len(sys.argv) > 1:
        coords = load_tsp(sys.argv[1])
        dist = build_dist_matrix(coords)
        run(dist, sys.argv[1])
    else:
        for n in [50, 100, 200]:
            coords = np.random.rand(n, 2) * 1000
            dist = build_dist_matrix(coords)
            run(dist, f"{n} random cities")
