import heapq
import random
import time

ROWS = 20
COLS = 20

# Create empty grid
def generate_grid():
    return [[0 for _ in range(COLS)] for _ in range(ROWS)]


# Dijkstra Algorithm (fixed)
def dijkstra(grid, start, goal):
    directions = [(0,1),(1,0),(0,-1),(-1,0)]
    pq = [(0, start)]

    distances = {start: 0}
    parent = {}

    while pq:
        cost, (x, y) = heapq.heappop(pq)

        if (x, y) == goal:
            path = []
            while (x, y) in parent:
                path.append((x, y))
                x, y = parent[(x, y)]
            path.append(start)
            return path[::-1]

        for dx, dy in directions:
            nx, ny = x + dx, y + dy

            if 0 <= nx < ROWS and 0 <= ny < COLS and grid[nx][ny] == 0:
                new_cost = cost + 1

                if (nx, ny) not in distances or new_cost < distances[(nx, ny)]:
                    distances[(nx, ny)] = new_cost
                    heapq.heappush(pq, (new_cost, (nx, ny)))
                    parent[(nx, ny)] = (x, y)

    return None


# Add dynamic obstacle
def add_dynamic_obstacle(grid, start, goal):
    while True:
        x = random.randint(0, ROWS-1)
        y = random.randint(0, COLS-1)

        # Avoid blocking start/goal
        if (x, y) != start and (x, y) != goal:
            grid[x][y] = 1
            break


# Print grid
def print_grid(grid, current, path=None):
    for i in range(ROWS):
        for j in range(COLS):
            if (i, j) == current:
                print("U", end=" ")  # UGV position
            elif (i, j) == (0, 0):
                print("S", end=" ")
            elif (i, j) == (ROWS-1, COLS-1):
                print("G", end=" ")
            elif path and (i, j) in path:
                print("*", end=" ")
            elif grid[i][j] == 1:
                print("#", end=" ")
            else:
                print(".", end=" ")
        print()
    print()


# Main
if __name__ == "__main__":
    grid = generate_grid()

    start = (0, 0)
    goal = (ROWS-1, COLS-1)

    current = start
    full_path = [current]

    start_time = time.time()

    while current != goal:
        path = dijkstra(grid, current, goal)

        if not path or len(path) < 2:
            print("❌ No path possible due to obstacles!")
            break

        # Move one step
        current = path[1]
        full_path.append(current)

        # Random dynamic obstacle
        if random.random() < 0.3:
            add_dynamic_obstacle(grid, start, goal)
            print("⚠ Dynamic obstacle added! Replanning...")

        print_grid(grid, current, path)

        time.sleep(0.2)  # slow for visualization

    end_time = time.time()

    if current == goal:
        print("✅ Goal reached!")
        print("Path length:", len(full_path))
        print("Time taken:", round(end_time - start_time, 4), "seconds")
    else:
        print("❌ Failed to reach goal.")