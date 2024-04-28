import cv2
import numpy as np
from FibonacciHeap import FibHeap
from priority_queue import FibPQ, HeapPQ, QueuePQ

class Maze:
    def __init__(self, maze_structure, start_point, end_point):
        self.maze_structure = maze_structure
        self.start_point = start_point
        self.end_point = end_point
        self.height, self.width = maze_structure.shape

def solve(maze):
    width = maze.width
    total = maze.width * maze.height

    start = maze.start_point
    end = maze.end_point

    visited = [False] * total
    prev = [None] * total
    infinity = float("inf")
    distances = [infinity] * total

    unvisited = HeapPQ()
    nodeindex = [None] * total

    distances[start[0] * width + start[1]] = 0
    startnode = FibHeap.Node(0, start)
    nodeindex[start[0] * width + start[1]] = startnode
    unvisited.insert(startnode)

    count = 0
    completed = False

    while len(unvisited) > 0:
        count += 1
        n = unvisited.removeminimum()
        u = n.value
        upos = u
        uposindex = upos[0] * width + upos[1]

        if distances[uposindex] == infinity:
            break

        if upos == end:
            completed = True
            break

        for v in get_neighbors(u, maze):
            vpos = v
            vposindex = vpos[0] * width + vpos[1]

            if not visited[vposindex]:
                d = abs(vpos[0] - upos[0]) + abs(vpos[1] - upos[1])
                newdistance = distances[uposindex] + d

                if newdistance < distances[vposindex]:
                    vnode = nodeindex[vposindex]
                    if vnode == None:
                        vnode = FibHeap.Node(newdistance, v)
                        unvisited.insert(vnode)
                        nodeindex[vposindex] = vnode
                        distances[vposindex] = newdistance
                        prev[vposindex] = u
                    else:
                        unvisited.decreasekey(vnode, newdistance)
                        distances[vposindex] = newdistance
                        prev[vposindex] = u

        visited[uposindex] = True

    path = reconstruct_path(prev, maze)
    return [path, [count, len(path), completed]]

def get_neighbors(cell, maze):
    x, y = cell
    neighbors = []
    for dx, dy in [(1, 0), (-1, 0), (0, 1), (0, -1)]:
        nx, ny = x + dx, y + dy
        if 0 <= nx < maze.height and 0 <= ny < maze.width and maze.maze_structure[nx, ny] == 1:
            neighbors.append((nx, ny))
    return neighbors

def reconstruct_path(prev, maze):
    width = maze.width
    start = maze.start_point
    end = maze.end_point
    path = []
    current = end
    while current != start:
        path.append(current)
        current = prev[current[0] * width + current[1]]
    path.append(start)
    path.reverse()
    return path

def display_solved_maze(maze_image, path):
    for point in path:
        x, y = point
        maze_image[x, y] = (0, 255, 0)  # Mark path cells in green
    cv2.imshow("Solved Maze", maze_image)
    cv2.waitKey(0)
    cv2.destroyAllWindows()

# Read the maze image
maze_image = cv2.imread("mazee.jpg")

# Preprocess the image
gray_image = cv2.cvtColor(maze_image, cv2.COLOR_BGR2GRAY)
_, binary_image = cv2.threshold(gray_image, 128, 255, cv2.THRESH_BINARY)

# Define the maze structure
maze_structure = binary_image // 255

# Specify start and end points
start_point = (10, 10)  # Example coordinates
end_point = (100, 100)   # Example coordinates

# Create the Maze object
maze = Maze(maze_structure, start_point, end_point)

# Solve the maze
path, stats = solve(maze)

# Display the solved maze
display_solved_maze(maze_image, path)
