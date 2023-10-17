class graphFunction(object):

    def __init__(self, fun):
        self.f = fun

    def getDomain(self, start: float, end: float, density: int):
        if end < start:
            end, start = start, end
        step: float = (end - start) / density
        continuity = False
        x = start
        dom = []
        for _ in range(density):
            try:
                if type(self.f(x)) != complex:
                    if not continuity:
                        continuity = True
                        dom.append(x)
            except ZeroDivisionError or ValueError:
                if continuity:
                    dom.append(x)
                    continuity = False
            finally:
                x += step
        return dom