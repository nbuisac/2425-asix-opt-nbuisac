from turtle import Turtle 
colors=["blue", "orange", "green", "yellow", "violet"]
t = Turtle()
t.speed(10)
FILES = False
COLUMNES = False

if FILES:
    files = len(colors)
else:
    files = 1
if COLUMNES:
    columnes = len(colors)
else:
    columnes = 1

files = 10
t.home()
t.clear()
ample = t.screen.window_width()
alt   = t.screen.window_height()
for i in range(files * columnes):
    t.up()
    if files == 1:
        x = -ample/2
    else:
        x = -ample/2 +(i * ample // columnes)
    if columnes == 1:
        y = alt/2
    else:
        y = alt/2 - (i * alt // files)
    t.goto(x, y)
    t.color(colors[i % len(colors)])
    t.down()
    t.begin_fill()
    t.forward(ample/columnes)
    t.right(90)
    t.forward(alt/files)
    t.right(90)
    t.forward(ample/columnes)
    t.right(90)
    t.forward(alt/files)
    t.right(90)
    t.end_fill()


t.screen.mainloop()