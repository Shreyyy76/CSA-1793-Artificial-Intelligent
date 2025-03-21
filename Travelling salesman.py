import itertools

def calculate_distance(route, distance_matrix):
    return sum(distance_matrix[route[i - 1]][route[i]] for i in range(len(route)))

def tsp_brute_force(distance_matrix):
    cities = list(range(len(distance_matrix)))
    min_distance = float('inf')
    best_route = None
    for route in itertools.permutations(cities):
        distance = calculate_distance(route, distance_matrix)
        if distance < min_distance:
            min_distance = distance
            best_route = route
    return best_route, min_distance

# Example usage
distance_matrix = [
    [0, 10, 15, 20],
    [10, 0, 35, 25],
    [15, 35, 0, 30],
    [20, 25, 30, 0]
]

best_route, min_distance = tsp_brute_force(distance_matrix)
print("Best route:", best_route)
print("Minimum distance:", min_distance)
