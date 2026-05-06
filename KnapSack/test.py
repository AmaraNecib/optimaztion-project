import time
from generate_data import generate_knapsack
from greedy import greedy_deterministic, greedy_nondeterministic
from local_search import local_search_first_improvement, local_search_best_improvement
from simulated_annealing import simulated_annealing
from genetic import genetic_algorithm


def run(n=50):
    items, capacity = generate_knapsack(n)
    print(f"\nKnapsack | n={n}  capacity={capacity}")
    print(f"{'Algorithm':<35} {'Value':>8} {'Time':>10}")
    print("-" * 56)

    tests = [
        ("Greedy Deterministic",           lambda: greedy_deterministic(items, capacity)),
        ("Greedy Nondeterministic",         lambda: greedy_nondeterministic(items, capacity)),
        ("Local Search First Improvement",  lambda: local_search_first_improvement(items, capacity)),
        ("Local Search Best Improvement",   lambda: local_search_best_improvement(items, capacity)),
        ("Simulated Annealing",             lambda: simulated_annealing(items, capacity)),
        ("Genetic Algorithm",               lambda: genetic_algorithm(items, capacity)),
    ]

    for name, fn in tests:
        t0 = time.perf_counter()
        val, _ = fn()
        elapsed = time.perf_counter() - t0
        print(f"{name:<35} {val:>8} {elapsed:>9.4f}s")


if __name__ == "__main__":
    for size in [50, 100, 200]:
        run(size)
