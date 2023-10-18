class GraphFunction(object):

    def __init__(self, fun):
        self.f = fun

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
            try:
                if type(self.f(x)) != complex:
                    if not continuity:
                        continuity = True
                        dom.append(x)
                else:
                    if continuity:
                        dom.append(x)
                        continuity = False
            except ZeroDivisionError or ValueError:
                if continuity:
                    dom.append(x)
                    continuity = False
            finally:
                x += step
        if continuity:
            dom.append(x)
        return dom
