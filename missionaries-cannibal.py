class State:
    def __init__(self, missionaries, cannibals, boat, parent=None):
        self.missionaries = missionaries
        self.cannibals = cannibals
        self.boat = boat
        self.parent = parent

    def is_valid(self):
        if self.missionaries < 0 or self.cannibals < 0 or self.missionaries > 3 or self.cannibals > 3:
            return False
        if (self.missionaries > 0 and self.missionaries < self.cannibals) or (3 - self.missionaries > 0 and 3 - self.missionaries < 3 - self.cannibals):
            return False
        return True

    def is_goal(self):
        return self.missionaries == 0 and self.cannibals == 0 and self.boat == 0

    def get_successors(self):
        successors = []
        if self.boat == 1:
            moves = [(-2, 0), (-1, -1), (0, -2), (-1, 0), (0, -1)]
        else:
            moves = [(2, 0), (1, 1), (0, 2), (1, 0), (0, 1)]

        for move in moves:
            new_state = State(self.missionaries + move[0], self.cannibals + move[1], 1 - self.boat, self)
            if new_state.is_valid():
                successors.append(new_state)
        return successors

    def __str__(self):
        return f"({self.missionaries}, {self.cannibals}, {'Left' if self.boat == 1 else 'Right'})"

def bfs(start_state):
    queue = [start_state]
    visited = set()
    visited.add((start_state.missionaries, start_state.cannibals, start_state.boat))

    while queue:
        current_state = queue.pop(0)
        if current_state.is_goal():
            return current_state

        for successor in current_state.get_successors():
            if (successor.missionaries, successor.cannibals, successor.boat) not in visited:
                visited.add((successor.missionaries, successor.cannibals, successor.boat))
                queue.append(successor)

    return None

def print_solution(solution_state):
    path = []
    current_state = solution_state
    while current_state:
        path.append(current_state)
        current_state = current_state.parent
    path.reverse()
    for state in path:
        print(state)

start_state = State(3, 3, 1)
solution = bfs(start_state)
if solution:
    print("Solution found! Step-by-step states are:")
    print_solution(solution)
else:
    print("No solution exists.")
