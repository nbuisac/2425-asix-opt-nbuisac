from turtle import Turtle 
t = Turtle()
t.speed(10)

costats = 6

angle = 360 / costats + 75

for i in range(100):
    for a in range(costats):
        t.forward(200)
        t.left(angle)


t.screen.mainloop()