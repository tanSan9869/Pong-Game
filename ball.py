from turtle import *

class Ball(Turtle):
        def __init__(self):
            super().__init__()
            self.shape("circle")
            self.color("white")
            self.penup()
            self.x_move=10
            self.y_move=10
            self.move_speed=0.1

        def moving_ball(self):
            new_x = self.xcor() + self.x_move
            new_y = self.ycor() + self.y_move
            self.goto(new_x,new_y)

        def bounce_y(self):
            self.y_move *=-1
            self.move_speed *=0.6

        def bounce_x(self):
            self.x_move *=-1

        def restart(self):
            self.goto(0,0)
            self.move_speed = 0.1
            self.bounce_x()
