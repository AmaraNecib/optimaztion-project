import random


def generate_knapsack(n, min_val=1, max_val=100):
    items = [
        {'v': random.randint(min_val, max_val), 'w': random.randint(min_val, max_val)}
        for _ in range(n)
    ]
    capacity = int(sum(item['w'] for item in items) * 0.5)
    return items, capacity


def generate_suite(sizes=(50, 100, 200, 500, 1000)):
    return {n: generate_knapsack(n) for n in sizes}
