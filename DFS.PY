# DFS Tower of Hanoi (3 Disks)
START_STATE = ((4, 3, ), (), ())
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

def dfs():
    stack = [(START_STATE, [START_STATE])]
    visited = set()
    while stack:
        state, path = stack.pop()
        if state == GOAL_STATE:
            return path
        if state in visited:
            continue
        visited.add(state)
        for move in get_possible_moves(state):
            stack.append((move, path + [move]))
    return None

solution = dfs()
if solution:
    print("DFS Solution:")
    for i, step in enumerate(solution):
        print(f"Step {i}: {step}")
    print("Total Moves:", len(solution) - 1)
else:
    print("No solution found")
