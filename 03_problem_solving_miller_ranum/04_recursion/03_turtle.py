import turtle

my_turtle = turtle.Turtle()
my_window = my_turtle.getscreen()

def draw_spiral(my_turtle: turtle.Turtle, 
                line_len: int) -> None:
    if line_len > 0:
        my_turtle.forward(line_len)
        my_turtle.right(90)
        draw_spiral(my_turtle, line_len-5)

if __name__ == '__main__':
    draw_spiral(my_turtle, 100)
    my_window.exitonclick()