import turtle

PART_OF_PATH = "0"
TRIED = "."
OBSTACLE = "+"
DEAD_END = "-"


class Maze:
    def __init__(self, maze_filename: str) -> None:
        rows_in_maze = 0
        cols_in_maze = 0
        self.maze_list = []
        maze_file = open(maze_filename, "r")
        for line in maze_file:
            row_list = []
            col = 0
            for ch in line[:-1]:
                row_list.append(ch)
                if ch == "S":
                    self.start_row = rows_in_maze
                    self.start_col = maze_col
                col += 1
            rows_in_maze += 1
            self.maze_list.append(row_list)

        self.rows_in_maze = rows_in_maze
        self.cols_in_maze = cols_in_maze

        self.x_translate = -1 * cols_in_maze / 2
        self.y_translate = -1 * rows_in_maze / 2
        self.t = turtle.Turtle()
        self.window = turtle.Screen()

    def draw_centered_box(self, x: int, y: int, color: str) -> None:
        self.t.up()
        self.t.goto(x - 0.5, y - 0.5)
        self.t.color(color)
        self.t.fillcolor(color)
        self.t.setheading(90)
        self.t.down()
        self.t.begin_fill()
        for _ in range(4):
            self.t.forward(1)
            self.t.right(90)
        self.t.end_fill()

    def draw_maze(self) -> None:
        self.t.speed(10)
        self.window.tracer(0)
        for y in range(self.rows_in_maze):
            for x in range(self.cols_in_maze):
                if self.maze_list[y][x] == OBSTACLE:
                    self.draw_centered_box(
                        x + self.x_translate, -1 * y + self.y_translate, "orange"
                    )
        self.t.color("black")
        self.t.fillcolor("blue")
        self.window.update()
        self.window.tracer(1)

    def move_turtle(self, x: int, y: int) -> None:
        self.t.up()
        self.t.setheading(
            self.t.towards(x + self.x_translate, -1 * y + self.y_translate)
        )
        self.t.goto(x + self.x_translate, -1 * y + self.y_translate)

    def drop_breadcrumb(self, color: str) -> None:
        self.t.dot(10, color)

    def update_position(self, row: int, col: int, val: str = None) -> None:
        if val:
            self.maze_list[row][col] = val
        self.move_turtle(col, row)

        if val == PART_OF_PATH:
            color = "green"
        elif val == OBSTACLE:
            color = "red"
        elif val == TRIED:
            color = "black"
        elif val == DEAD_END:
            color = "red"
        else:
            color = None

        if color:
            self.drop_breadcrumb(color)

    def is_exit(self, row: int, col: int) -> bool:
        return (
            row == 0
            or row == self.rows_in_maze - 1
            or col == 0
            or col == self.cols_in_maze - 1
        )

    def __getitem__(self, idx: int) -> str:
        return self.maze_list[idx]


def search_from(maze: Maze, start_row: int, start_col: int) -> bool:

    # try each of four directions from this point until we find a way out.

    # base case return values:
    # 1. We have run into an obstacle, return False
    maze.update_position(start_row, start_col)
    if maze[start_row][start_col] == OBSTACLE:
        return False
    # 2. We have found a square that has already been explored
    if maze[start_row][start_col] in (TRIED, DEAD_END):
        return False
    # 3. We have found an outside edge not occupied by an obstacle
    if maze.is_exit(start_row, start_col):
        maze.update_position(start_row, start_col, PART_OF_PATH)
        return True
    maze.update_position(start_row, start_col, TRIED)
    # Otherwise, use logical short circuiting to try each direction
    # in turn (if needed)
    found = (
        search_from(maze, start_row - 1, start_col)
        or search_from(maze, start_row + 1, start_col)
        or search_from(maze, start_row, start_col - 1)
        or search_from(maze, start_row, start_col + 1)
    )
    if found:
        maze.update_position(start_row, start_col, PART_OF_PATH)
    else:
        maze.update_position(start_row, start_col, DEAD_END)
    return found
