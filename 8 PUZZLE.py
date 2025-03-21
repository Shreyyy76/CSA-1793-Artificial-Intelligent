import heapq

class PuzzleState:
    def __init__(self, board, parent=None, move=0, cost=0):
        self.board = board
        self.parent = parent
        self.move = move
        self.cost = cost
        self.heuristic = self.calculate_heuristic()
        self.priority = self.cost + self.heuristic

    def calculate_heuristic(self):
        goal = [1, 2, 3, 4, 5, 6, 7, 8, 0]
        distance = 0
        for i in range(9):
            if self.board[i] != 0:
                goal_index = goal.index(self.board[i])
                current_row, current_col = divmod(i, 3)
                goal_row, goal_col = divmod(goal_index, 3)
                distance += abs(current_row - goal_row) + abs(current_col - goal_col)
        return distance

    def get_neighbors(self):
        neighbors = []
        zero_index = self.board.index(0)
        moves = [(-1, 0), (1, 0), (0, -1), (0, 1)]
        for move_row, move_col in moves:
            new_row = zero_index // 3 + move_row
            new_col = zero_index % 3 + move_col
            if 0 <= new_row < 3 and 0 <= new_col < 3:
                new_zero_index = new_row * 3 + new_col
                new_board = self.board[:]
                new_board[zero_index], new_board[new_zero_index] = new_board[new_zero_index], new_board[zero_index]
                neighbors.append(PuzzleState(new_board, self, self.move + 1, self.cost + 1))
        return neighbors

    def __lt__(self, other):
        return self.priority < other.priority

def solve_puzzle(start_board):
    start_state = PuzzleState(start_board)
    goal_board = [1, 2, 3, 4, 5, 6, 7, 8, 0]
    open_list = []
    closed_list = set()
    heapq.heappush(open_list, start_state)

    while open_list:
        current_state = heapq.heappop(open_list)
        if current_state.board == goal_board:
            solution_path = []
            while current_state:
                solution_path.append(current_state.board)
                current_state = current_state.parent
            return solution_path[::-1]
        closed_list.add(tuple(current_state.board))
        for neighbor in current_state.get_neighbors():
            if tuple(neighbor.board) not in closed_list:
                heapq.heappush(open_list, neighbor)

    return None

start_board = [1, 2, 3, 4, 5, 6, 0, 7, 8]
solution = solve_puzzle(start_board)
if solution:
    for step in solution:
        for i in range(3):
            print(step[i*3:(i+1)*3])
        print()
else:
    print("No solution found.")
