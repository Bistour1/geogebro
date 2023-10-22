import copy
import turtle
from math import sin, cos, tan, exp, pi, log, log2, log10
import time
import screeninfo
from GraphFunction import GraphFunction
import tkinter

# width / (zoom*30) = maxLimit
# width / (zoom*300) = unitary grade

retrace_parameters = {}
retrace_funs = []
def main():
    def quit():
        root.destroy()


    root = tkinter.Tk()
    root.title("GEOGEBRO")
    root.resizable(width= True, height=True)
    bar = tkinter.Menu(root)
    fileMenu = tkinter.Menu(bar, tearoff=0)
    fileMenu.add_command(label="Exit", command=quit)
    bar.add_cascade(label="File", menu=fileMenu)
    root.config(menu= bar)
    mainFrame = tkinter.Frame(root, borderwidth=1, padx=5, pady=5)
    mainFrame.pack()
    root.geometry("400x250+300+300")
    canvas = tkinter.Canvas(mainFrame)
    canvas.pack()
    canvas.create_line(0,0,100,100)

    tkinter.mainloop()



def retrace(x, y):
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
    turtle.clearscreen()
    parameters = copy.deepcopy(retrace_parameters)
    funs = copy.deepcopy(retrace_funs)
    turtle.tracer(0,0)
    for f in funs:
        params = {}
        for _ in range(f.__code__.co_argcount):
            k = list(parameters.keys())[0]
            p = parameters.pop(k)
            if not (p is None):
                params[k] = p
        f(**params)
    turtle.update()
    return turtle.getscreen()
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


    #graduations
    graduation = int(width//(zoom*10))

    number_x_graduation = int(width//(graduation*zoom))
    number_y_graduation = int(height//(graduation*zoom))

    #graduation x
    for i in range(number_x_graduation*2+1):
        turtle.penup()
        turtle.goto(graduation*zoom*(i-number_x_graduation),-10)
        turtle.pendown()
        turtle.goto(graduation*zoom*(i-number_x_graduation),10)
        turtle.write(graduation*(i-number_x_graduation))

    #graduation y
    for i in range(number_y_graduation*2+1):
        turtle.penup()
        turtle.goto(-10, graduation*zoom*(i-number_y_graduation))
        turtle.pendown()
        turtle.goto(10, graduation*zoom*(i-number_y_graduation))
        turtle.write(graduation*(i-number_y_graduation))

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
    main()

"""
    turtle.clearscreen()
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
    retrace_parameters = {"zoom": zoom,"fun": f,"zoomParameter": zoom, "color": None}
    retrace_funs = trace_axis,trace_function
    turtle.getscreen().onclick(retrace)
    turtle.getscreen().listen()
    retrace(0, 0)
    turtle.done()
    """