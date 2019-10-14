import turtle

def draw_square(side_length):
    side_count = 0
    while side_count < 4:
        turtle.forward(side_length)
        turtle.left(90)
        side_count += 1

def draw_triangle(side_length):
    side_count = 0
    while side_count < 3:
        turtle.forward(side_length)
        turtle.left(120)
        side_count += 1

degrees = 0
degree_increment = 5
while degrees < 360:
    turtle.color('blue')
    draw_triangle(300)
    turtle.color('green')
    draw_square(200)
    turtle.left(degree_increment)
    degrees += degree_increment

input("type enter to stop ")
