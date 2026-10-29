import queue

GOAL_STATE = (1, 2, 3, 
              4, 5, 6, 
              7, 8, 0) 

def get_pos(state, value):
    idx = state.index(value)
    return idx // 3, idx % 3

def manhattan_distance(state):
    distance = 0
    for i in range(9):
        value = state[i]
        if value != 0: 
            current_row, current_col = i // 3, i % 3
            goal_row, goal_col = get_pos(GOAL_STATE, value)
            distance += abs(current_row - goal_row) + abs(current_col - goal_col)
    return distance

def get_neighbors(state):
    neighbors = []
    blank_idx = state.index(0)
    row, col = blank_idx // 3, blank_idx % 3
    
    moves = [(-1, 0), (1, 0), (0, -1), (0, 1)]
    
    for dr, dc in moves:
        new_row, new_col = row + dr, col + dc
        
        if 0 <= new_row < 3 and 0 <= new_col < 3:
            new_blank_idx = new_row * 3 + new_col
            
            new_state = list(state)
            new_state[blank_idx], new_state[new_blank_idx] = new_state[new_blank_idx], new_state[blank_idx]
            neighbors.append(tuple(new_state))
            
    return neighbors

# The A* Search Algorithm
def solve_8_puzzle(initial_state):
    pq = queue.PriorityQueue()
    
    h_initial = manhattan_distance(initial_state)
    pq.put((h_initial, initial_state, [initial_state]))
    
    visited = set()
    visited.add(initial_state)
    
    while not pq.empty():
        f, current, path = pq.get()
        
        if current == GOAL_STATE:
            return path
            
        g = len(path) - 1 
        
        for neighbor in get_neighbors(current):
            if neighbor not in visited:
                visited.add(neighbor)
                h = manhattan_distance(neighbor)
                f_new = (g + 1) + h
                
                pq.put((f_new, neighbor, path + [neighbor]))
                
    return None

def print_board(state):
    for i in range(0, 9, 3):
        print(state[i], state[i+1], state[state[i+2]])
    print("-" * 10)

if __name__ == "__main__":
    initial = (1, 2, 3, 
               4, 5, 0, 
               7, 8, 6)
    
    print("Initial State:")
    print_board(initial)
    
    solution_path = solve_8_puzzle(initial)
    
    if solution_path:
        print(f"Goal reached in {len(solution_path) - 1} moves!\n")
        print("Path to Goal:")
        for step, state in enumerate(solution_path):
            print(f"Step {step}:")
            print_board(state)
    else:
        print("No solution found.")
