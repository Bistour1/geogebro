import turtle
from math import sin, cos, tan, exp, pi
import time
import screeninfo


def retrace(parameters,*funs):
    i = 0
    for f in funs:
        params = []
        for j in range(f.__code__.co_argcount):
            params.append(parameters[i+j])
        i += f.__code__.co_argcount
        params = tuple(params)
        f(*params)
def trace_axis(zoom=1):
    turtle.tracer(0,0)
    height = int(turtle.window_height() // 2)
    width = int(turtle.window_width() // 2)
    turtle.penup()
    turtle.color("black")
    turtle.goto(-1*width, 0)
    turtle.pendown()
    turtle.goto(width, 0)
    turtle.penup()
    turtle.goto(width - 20, 20)
    turtle.pendown()
    turtle.write("x", font=("Arial", 20, "normal"))
    turtle.penup()
    turtle.goto(width, 0)
    turtle.pendown()
    turtle.goto(0, 0)
    turtle.goto(0, height)
    turtle.penup()
    turtle.goto(20, height - 30)
    turtle.pendown()
    turtle.write("y", font=("Arial", 20, "normal"))
    turtle.penup()
    turtle.goto(0, height)
    turtle.pendown()
    turtle.goto(0, -1*height)
    turtle.update()


def trace_function(fun, zoomParameter = 1):
    """

    :param fun: function to be traced
    :type fun: function
    """
    turtle.tracer(0,0)
    height = int(turtle.window_height() // 2)
    width = int(turtle.window_width() // 2)
    zoomParameter = zoomParameter * 30
    if zoomParameter == 0:
        zoomParameter = 1
    turtle.color("red")
    turtle.penup()
    if type(fun(-1*width / zoomParameter)*zoomParameter) != complex:
        turtle.goto(-1*width, int(max(min(int(fun(-1*width / zoomParameter) * zoomParameter), height), -1*height)))
    turtle.pendown()
    for i in range(-1*width, width):
        if type(fun(i / zoomParameter)*zoomParameter) != complex:
            turtle.goto(i, max(min(fun(i / zoomParameter) * zoomParameter, height), -1*height))
    turtle.update()


if __name__ == "__main__":
    turtle.clear()
    screenWidth = 0
    screenHeight = 0
    for m in screeninfo.get_monitors():
        if(m.is_primary):
            screenWidth = m.width
            screenHeight = m.height
    turtle.setup(width=screenWidth-20,height=screenHeight-20,startx=0,starty=0)
    turtle.hideturtle()
    turtle.speed("fastest")
    f = eval("lambda x: " + turtle.textinput("Parameters","function :"))
    zoom = float(turtle.numinput("parameter","zoom = "))
    turtle.onclick(retrace([zoom,f,zoom], trace_axis,trace_function),"f")
    turtle.listen()
    turtle.mainloop()