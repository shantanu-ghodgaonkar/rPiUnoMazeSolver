import cv2
from point import Point

CELL_SIZE = 20
EMPTY_CELL = [255 for _ in range(CELL_SIZE)]
GAP_THRESHOLD = CELL_SIZE - 5

# A class to store the x and y coordinate of a point
# The + and = operators are overloaded to work for it


class MazeSolverBFS:
    """_summary_
    """

    def __init__(self, start: Point, img):
        self.start = start
        self.end = Point()
        self.img = img
        self.h, self.w = img.shape[:2]
        self.found = False
        self.queue = []
        self.visited = [[0 for j in range(self.w)] for i in range(self.h)]
        self.parent = [[Point() for j in range(self.w)] for i in range(self.h)]
        self.queue.append(self.start)
        self.visited[self.start.y][self.start.x] = 1
        self.path = []
        # TODO: Calibrate this directions variable
        # self.directions = [Point(0, -(CELL_SIZE/2)), Point(0, (CELL_SIZE/2)),
        #                    Point((CELL_SIZE/2), 0), Point(-(CELL_SIZE/2), 0)]
        self.directions = [Point(0, -1), Point(0, 1),
                           Point(1, 0), Point(-1, 0)]

    def find_end(self) -> None:
        i = 0
        endFound = False
        while i < self.img.shape[0]:
            left_wall_white_px_count = sum(1 for element in (
                self.img[i:i+CELL_SIZE, 0] == EMPTY_CELL) if element)
            right_wall_white_px_count = sum(1 for element in (
                self.img[i:i+CELL_SIZE, self.img.shape[0]-1] == EMPTY_CELL) if element)
            up_wall_white_px_count = sum(1 for element in (
                self.img[0, i:i+CELL_SIZE] == EMPTY_CELL) if element)
            down_wall_white_px_count = sum(1 for element in (
                self.img[self.img.shape[0]-1, i:i+CELL_SIZE] == EMPTY_CELL) if element)
            if left_wall_white_px_count > GAP_THRESHOLD:
                endFound = True
                self.end = Point(0, i + int(CELL_SIZE/2))
                print(f"Gap found at = ({self.end.x}, {self.end.y})")
                break
            elif right_wall_white_px_count > GAP_THRESHOLD:
                endFound = True
                self.end = Point(299, i + int(CELL_SIZE/2))
                print(f"Gap found at = ({self.end.x}, {self.end.y})")
                break
            elif up_wall_white_px_count > GAP_THRESHOLD:
                endFound = True
                self.end = Point(i + int(CELL_SIZE/2), 0)
                print(f"Gap found at = ({self.end.x}, {self.end.y})")
                break
            elif down_wall_white_px_count > GAP_THRESHOLD:
                endFound = True
                self.end = Point(i + int(CELL_SIZE/2), 299)
                print(f"Gap found at = ({self.end.x}, {self.end.y})")
                break
            else:
                pass
            i += CELL_SIZE
        if not endFound:
            print(f"Gap not found, please recalibrate parameters")

    def solve_maze(self) -> list:
        self.img = cv2.cvtColor(self.img, cv2.COLOR_GRAY2BGR)
        while len(self.queue) > 0:
            # popping one element from queue and storing in p
            p = self.queue.pop(0)

            # surrounding elements
            for d in self.directions:
                cell = p + d

                # if cell(a surrounding pixel) is in range of image, not visited, !(B==0 && G==0 && R==0) i.e. pixel is
                # not black as black represents border
                if (0 <= cell.x < self.w and 0 <= cell.y < self.h and
                    self.visited[cell.y][cell.x] == 0
                    and
                        (self.img[cell.y][cell.x][0] != 0 or self.img[cell.y][cell.x][1] != 0 or self.img[cell.y][cell.x][2] != 0)):

                    self.queue.append(cell)

                    # marking cell as visited
                    self.visited[cell.y][cell.x] = 1
                    # changing the pixel color to red
                    self.img[cell.y][cell.x] = [0, 0, 255]

                    # string the value of p in parent matrix to trace path
                    self.parent[cell.y][cell.x] = p

                    # if end is found break
                    if cell == self.end:
                        self.found = True
                        del self.queue[:]
                        break

        # list to trace path
        self.path = []
        if self.found:
            p = self.end

            while p != self.start:
                self.path.append(p)
                p = self.parent[p.y][p.x]

            self.path.append(p)
            self.path.reverse()

        # changing the pixel of resulting path to white
        for p in self.path:
            self.img[p.y][p.x] = [255, 255, 255]

    def show_img(self):
        cv2.imshow("maze photo", self.img)
        cv2.waitKey(0)
        cv2.destroyAllWindows()
