import numpy as np


def load_tsp(filename):
    """Parse a TSPLIB .tsp file and return coordinate array."""
    coords = []
    with open(filename) as f:
        reading = False
        for line in f:
            line = line.strip()
            if line == 'NODE_COORD_SECTION':
                reading = True
                continue
            if line in ('EOF', ''):
                if reading:
                    break
                continue
            if reading:
                parts = line.split()
                if len(parts) >= 3:
                    coords.append((float(parts[1]), float(parts[2])))
    return np.array(coords)


def build_dist_matrix(coords):
    n = len(coords)
    d = np.zeros((n, n))
    for i in range(n):
        for j in range(i + 1, n):
            dist = np.linalg.norm(coords[i] - coords[j])
            d[i, j] = d[j, i] = dist
    return d


def tour_length(route, dist):
    n = len(route)
    return sum(dist[route[i], route[(i + 1) % n]] for i in range(n))
