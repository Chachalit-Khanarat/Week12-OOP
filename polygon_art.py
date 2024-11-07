import turtle
import random

class Polygon():
    def __init__(self, num_sides, size, orientation, location = [], color = (0,0,0), border_size = 1):
        self.side = num_sides
        self.size = size
        self.orientation = orientation
        self.location = location
        self.color = color
        self.border_size = border_size
        
    def draw_polygon(self):
        turtle.penup()
        turtle.goto(self.location[0], self.location[1])
        turtle.setheading(self.orientation)
        turtle.color(self.color)
        turtle.pensize(self.border_size)
        turtle.pendown()
        for _ in range(self.side):
            turtle.forward(self.size)
            turtle.left(360/self.side)
        turtle.penup()

class Run():
    def __init__(self, choice):
        self.choice = choice
        self.num = random.randint(20,40)
        self.choice_choose()
        
    def get_new_color(self):
        return (random.randint(0, 255), random.randint(0, 255), random.randint(0, 255))
        
    def choice_choose(self):
        match self.choice:
            case 1 :
                for i in range(self.num):
                    p = Polygon(3, random.randint(50,150), 
                                random.randint(0, 90), 
                                [random.randint(-300, 300), random.randint(-200, 200)], 
                                self.get_new_color(), 
                                border_size=random.randint(1, 10))
                    p.draw_polygon()
            case 2 :
                for i in range(self.num):
                    p = Polygon(4, random.randint(50,150), 
                                random.randint(0, 90), 
                                [random.randint(-300, 300), random.randint(-200, 200)], 
                                self.get_new_color(), 
                                border_size=random.randint(1, 10))
                    p.draw_polygon()
            case 3 :
                for i in range(self.num):
                    p = Polygon(5, random.randint(50,150), 
                                random.randint(0, 90), 
                                [random.randint(-300, 300), random.randint(-200, 200)], 
                                self.get_new_color(), 
                                border_size=random.randint(1, 10))
                    p.draw_polygon()
            case 4 :
                for i in range(self.num):
                    p = Polygon(random.randint(3,5), 
                                random.randint(50,150), 
                                random.randint(0, 90), 
                                [random.randint(-300, 300), random.randint(-200, 200)], 
                                self.get_new_color(), 
                                border_size=random.randint(1, 10))
                    p.draw_polygon()         
            case 5 :
                for i in range(self.num):
                    p = EmbeddedPolygon(3, random.randint(50,150), 
                                        random.randint(0, 90), 
                                        [random.randint(-300, 300), random.randint(-200, 200)], 
                                        self.get_new_color(), 
                                        border_size=random.randint(1, 10))
                    p.draw_polygon()
            case 6 :
                for i in range(self.num):
                    p = EmbeddedPolygon(4, random.randint(50,150), 
                                        random.randint(0, 90), 
                                        [random.randint(-300, 300), random.randint(-200, 200)], 
                                        self.get_new_color(), 
                                        border_size=random.randint(1, 10))
                    p.draw_polygon()
            case 7 :
                for i in range(self.num):
                    p = EmbeddedPolygon(5, random.randint(50,150), 
                                        random.randint(0, 90), 
                                        [random.randint(-300, 300), random.randint(-200, 200)], 
                                        self.get_new_color(), 
                                        border_size=random.randint(1, 10))
                    p.draw_polygon()
            case 8 :
                for i in range(self.num):
                    p = EmbeddedPolygon(random.randint(3, 5), 
                                        random.randint(50,150), 
                                        random.randint(0, 90), 
                                        [random.randint(-300, 300), random.randint(-200, 200)],
                                        self.get_new_color(), 
                                        border_size=random.randint(1, 10))
                    p.draw_polygon()
            case 9 :
                for i in range(self.num):
                    p = random.choice([EmbeddedPolygon(random.randint(3, 5), 
                                                       random.randint(50,150), 
                                                       random.randint(0, 90), 
                                                       [random.randint(-300, 300), random.randint(-200, 200)], 
                                                       self.get_new_color(), 
                                                       border_size=random.randint(1, 10)),
                                        Polygon(random.randint(3,5), 
                                                random.randint(50,150), 
                                                random.randint(0, 90), 
                                                [random.randint(-300, 300), 
                                                 random.randint(-200, 200)], 
                                                self.get_new_color(), 
                                                border_size=random.randint(1, 10))])
                    p.draw_polygon()


class EmbeddedPolygon(Polygon): 
    
    def draw_polygon(self):
        reduction_ratio = 0.618
        for i in range(3):
            turtle.penup()
            turtle.goto(self.location[0], self.location[1])
            turtle.setheading(self.orientation)
            turtle.color(self.color)
            turtle.pensize(self.border_size)
            turtle.pendown()
            for _ in range(self.side):
                turtle.forward(self.size)
                turtle.left(360/self.side)
                
            turtle.penup()
            turtle.forward(self.size*(1-reduction_ratio)/2)
            turtle.left(90)
            turtle.forward(self.size*(1-reduction_ratio)/2)
            turtle.right(90)
            self.location[0] = turtle.pos()[0]
            self.location[1] = turtle.pos()[1]
            self.size *= reduction_ratio
            

turtle.speed(0)
turtle.bgcolor('black')
turtle.tracer(0)
turtle.colormode(255)

_in = int(input())
Run(_in)

turtle.done()