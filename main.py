import turtle
from math import sin, cos, tan, exp, pi, log, log2, log10
import time
import screeninfo
from GraphFunction import GraphFunction


def retrace(parameters,*funs):
    """
    execute all the given function with the given parameters\n
    you have to give as many parameters as the functions ask

    :param parameters: arguments to give to the functions
    :type parameters: list
    :param funs: functions you want to execute
    :type funs: function
    :return: None
    :rtype: None
    """
    i = 0

    for f in funs:
        params = []
        for j in range(f.__code__.co_argcount):
            params.append(parameters[i+j])
        i += f.__code__.co_argcount
        params = tuple(params)
        f(*params)
def trace_axis(zoom=1.0):
    """
    Trace the x and y axis with the given zoom.\n
    the zoom parameter doesn't make anything for now but will be useful when
    graduations are added.

    :param zoom: zoom of the screen
    :type zoom: float
    :return: None
    :rtype: None
    """


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
    Trace the give function in red

    :param fun: function to be traced
    :type fun: GraphFunction
    """
    turtle.tracer(0,0)
    height = int(turtle.window_height() // 2)
    width = int(turtle.window_width() // 2)
    zoomParameter = zoomParameter * 30
    if zoomParameter == 0:
        zoomParameter = 1
    turtle.color("red")
    turtle.penup()
    left_limit = -1*width/zoomParameter
    right_limit = width/zoomParameter
    domain = fun.getDomain(left_limit,right_limit, 2*width)
    step = 1/zoomParameter
    x = left_limit
    turtle.penup()
    continuous = False
    for i in range(2*width):
        if x in domain:
            continuous = not continuous
        else:
            if continuous:
                turtle.goto(i - width, fun.f(x) * zoomParameter)
                turtle.pendown()
            else:
                turtle.penup()
        x += step
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
    f = GraphFunction(turtle.textinput("Parameters","function :"))
    zoom = float(turtle.numinput("parameter","zoom = "))
    turtle.onclick(retrace([zoom,f,zoom], trace_axis,trace_function),"f")
    turtle.listen()
    turtle.mainloop()