from collections import deque

# BFS Tower of Hanoi (3 Disks)
START_STATE = ((4, 3, 2), (), ())
GOAL_STATE = ((), (), (4, 3, 2))

def get_possible_moves(state):
    moves = []
    pegs = [list(p) for p in state]
    for i in range(3):
        if not pegs[i]:
            continue
        disk = pegs[i][-1]
        for j in range(3):
            if i != j and (not pegs[j] or pegs[j][-1] > disk):
                new_pegs = [list(p) for p in pegs]
                new_pegs[i].pop()
                new_pegs[j].append(disk)
                moves.append(tuple(tuple(p) for p in new_pegs))
    return moves

def bfs():
    queue = deque([(START_STATE, [START_STATE])])
    visited = set()
    while queue:
        state, path = queue.popleft()
        if state == GOAL_STATE:
            return path
        if state in visited:
            continue
        visited.add(state)
        for move in get_possible_moves(state):
            queue.append((move, path + [move]))
    return None

solution = bfs()
if solution:
    print("BFS Solution:")
    for i, step in enumerate(solution):
        print(f"Step {i}: {step}")
    print("Total Moves:", len(solution) - 1)
else:
    print("No solution found")
