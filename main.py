import turtle
from math import sin, cos, tan, exp, pi, log, log2, log10
import time
import screeninfo
from GraphFunction import GraphFunction

# width / (zoom*30) = maxLimit
# width / (zoom*300) = unitary grade


def retrace(parameters,*funs):
    """
    execute all the given function with the given parameters\n
    you have to give as many parameters as the functions ask and name it

    :param parameters: keywords arguments to give to the functions
    :type parameters: dict
    :param funs: functions you want to execute
    :type funs: function
    :return: None
    :rtype: None
    """

    for f in funs:
        params = {}
        for _ in range(f.__code__.co_argcount):
            k = list(parameters.keys())[0]
            p = parameters.pop(k)
            if not (p is None):
                params[k] = p
        f(**params)
        turtle.update()
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

    # axe x
    height = int(turtle.window_height() // 2)
    width = int(turtle.window_width() // 2)

    zoom *= 30

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

    #axe y
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

    #graduation x
    turtle.penup()
    turtle.goto(width/10,-10)
    turtle.pendown()
    turtle.goto(width/10,10)
    turtle.write(width/(zoom*10))

# x' = x/zoom -> x = zoom * x'
def trace_function(fun, zoomParameter = 1, color = "red"):
    """
    Trace the give function in red

    :param fun: function to be traced
    :type fun: GraphFunction
    """
    turtle.tracer(0,0)
    height = int(turtle.window_height() // 2)
    width = int(turtle.window_width() // 2)
    zoomParameter *= 30
    if zoomParameter == 0:
        zoomParameter = 1
    turtle.color(color)
    turtle.penup()
    left_limit = -1*width/zoomParameter
    right_limit = width/zoomParameter
    domain = fun.getDomain(left_limit,right_limit, 2*width)
    step = 1/zoomParameter
    turtle.penup()
    continuous = False
    for i,x in zip(range(2*width),list(left_limit + a*step for a in range(2*width))):
        if x in domain:
            continuous = not continuous
        else:
            if continuous:
                turtle.goto(i - width, max(min(fun.f(x) * zoomParameter,height),-1*height))
                turtle.pendown()
            else:
                turtle.penup()


if __name__ == "__main__":
    turtle.clear()
    screenWidth = 0
    screenHeight = 0
    for m in screeninfo.get_monitors():
        if(m.is_primary):
            screenWidth = m.width
            screenHeight = m.height

    print(screenWidth)
    turtle.setup(width=screenWidth-20,height=screenHeight-20,startx=0,starty=0)
    turtle.hideturtle()
    turtle.speed("fastest")
    f = GraphFunction(turtle.textinput("Parameters","function :"))
    zoom = float(turtle.numinput("parameter","zoom = "))
    turtle.onclick(retrace({"zoom": zoom,"fun": f,"zoomParameter": zoom, "color": None}, trace_axis,trace_function),"f")
    turtle.listen()
    turtle.mainloop()