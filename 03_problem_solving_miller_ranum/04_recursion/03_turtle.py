import turtle
from collections import namedtuple
from typing import List
import math


def draw_spiral(t: turtle.Turtle, 
                line_len: int) -> None:
    if line_len > 0:
        t.forward(line_len)
        t.right(90)
        draw_spiral(t, line_len-5)


def draw_tree(t: turtle.Turtle, 
              branch_len: int) -> None:
    if branch_len > 5:
        t.forward(branch_len)
        t.right(20)
        draw_tree(branch_len - 15, t)
        t.left(40)
        draw_tree(branch_len - 15, t)
        t.right(20)
        t.backward(branch_len)


Point = namedtuple('Point', ['x', 'y'])


def draw_sierpinski(
    t: turtle.Turtle,
    points: List[Point],
    degree: int) -> None:

    def draw_triangle(
        t: turtle.Turtle,
        points: List[Point],
        color: str
        ) -> None:

        t.fillcolor(color)
        t.up()
        t.goto(points[0].x, points[0].y)
        t.down()
        t.begin_fill()
        t.goto(points[1].x, points[1].y)
        t.goto(points[2].x, points[2].y)
        t.goto(points[0].x, points[0].y)
        t.end_fill()

    def get_mid(
        p1: Point,
        p2: Point
        ) -> Point:

        return Point((p1.x + p2.x) / 2, (p1.y + p2.y) / 2)

    colormap = ['blue', 'red', 'green', 'white']
    draw_triangle(t, points, colormap[degree])
    if degree > 0:
        draw_sierpinski(t,
                        [points[0],
                         get_mid(points[0], points[1]),
                         get_mid(points[0], points[2])],
                        degree - 1
                        )
        draw_sierpinski(t,
                        [points[1],
                         get_mid(points[1], points[0]),
                         get_mid(points[1], points[2])],
                        degree - 1
                        )
        draw_sierpinski(t,
                        [points[2],
                         get_mid(points[2], points[0]),
                         get_mid(points[2], points[1])],
                        degree - 1
                        )


if __name__ == '__main__':
    my_turtle = turtle.Turtle()
    my_window = turtle.Screen()

    # # Draw Spiral
    # draw_spiral(my_turtle, 100)

    # # Draw Tree
    # my_turtle.left(90)
    # my_turtle.up()
    # my_turtle.backward(100)
    # my_turtle.down()
    # my_turtle.color("green")
    # draw_tree(75, my_turtle)
    # my_window.exitonclick()
    
    # Draw Sierpinski
    my_points = [
        Point(-100, -50),
        Point(0, -50 + math.sqrt(3) * 100),
        Point(100, 50)
    ]
    draw_sierpinski(my_points, 3, my_turtle)
    my_window.exitonclick()
