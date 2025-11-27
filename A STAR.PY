import heapq

# A* Tower of Hanoi (3 Disks)
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

def heuristic(state):
    # Number of disks not on goal peg
    return 3 - len(state[2])

def astar():
    pq = []
    heapq.heappush(pq, (0, START_STATE, [START_STATE]))
    visited = set()
    while pq:
        cost, state, path = heapq.heappop(pq)
        if state == GOAL_STATE:
            return path
        if state in visited:
            continue
        visited.add(state)
        for move in get_possible_moves(state):
            g = len(path)
            h = heuristic(move)
            f = g + h
            heapq.heappush(pq, (f, move, path + [move]))
    return None

solution = astar()
if solution:
    print("A* Solution:")
    for i, step in enumerate(solution):
        print(f"Step {i}: {step}")
    print("Total Moves:", len(solution) - 1)
else:
    print("No solution found")
