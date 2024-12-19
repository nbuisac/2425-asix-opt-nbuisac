from turtle import Turtle 
t = Turtle()
t.speed(10)

colors = ["red", "blue"]
t.home()
t.clear()
ample = t.screen.window_width()
alt   = t.screen.window_height()
t.up()
t.goto(-ample/2, alt/2)
t.down()
FILES = 16
for a in range(FILES):
    t.color(colors[a % len(colors)])
    t.begin_fill()
    t.forward(ample)
    t.right(90)
    t.forward(alt/FILES)
    t.right(90)
    t.forward(ample)
    t.end_fill()
    t.left(180) # girem 180 graus


t.screen.mainloop()