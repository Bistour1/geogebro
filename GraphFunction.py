from math import sin, cos, tan, exp, pi, log, log2, log10


class GraphFunction(object):

    def __init__(self, funString):
        self.funString = funString
        self.f = eval(f"lambda x: {funString}")

    def __str__(self):
        return f"GraphFunction:(function : {self.funString})"

    def getDomain(self, start: float, end: float, density: int):
        """
        Return the domain of the function between start and end.\n
        the format of the domain is a list of floats:\n
        - the first number is the start of the domain\n
        - the second closes the domain\n
        - the third one reopens it\n
        - etc...\n
        example : [4;6]U[8;13] => [4, 6, 8, 13]


        :param start: start of the domain to check
        :type start: float
        :param end: end of the domain to check
        :type end: float
        :param density: how many numbers there are to check in the domain
        :type density: int
        :return: domain of the function
        :rtype: list
        """
        if end < start:
            end, start = start, end
        step: float = (end - start) / density
        continuity = False  # bool saying if the area is defined by the function or not
        x = start
        dom = []  # list to store result
        for _ in range(density):  # check for each number if the function is defined at that point
            if self.inDomain(x) != continuity:
                continuity = not continuity
                dom.append(x)
            x += step
        if continuity:
            dom.append(x)
        return dom

    def inDomain(self, x: float):
        """
        Check if a number is in the domain of the function

        :param x: number to check
        :type x: float
        :return: if x is in the domain of f
        :rtype: bool
        """
        try:
            if type(self.f(x)) != complex:
                return True
            return False
        except ZeroDivisionError:
            return False
        except ValueError:
            return False
