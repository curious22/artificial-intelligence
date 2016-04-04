import math


class BaseFunctions(object):
    def __init__(self, numb_of_layers, neurons_in_layer, a, b, k, t, h, m):
        self.layers = numb_of_layers
        self.neurons = neurons_in_layer

        self.V = 0
        self.y = 0

        self.a = a
        self.b = b
        self.k = k
        self.t = t
        self.h = h
        self.m = m

    conf_round = lambda x: round(x, 3)

    def counting_number_neurons(self):
        self.V = self.layers * self.neurons

    def func1(self):
        if self.V > self.a:
            return 1
        else:
            return 0

    def func2(self):
        return math.exp(self.V * - 1)

    def func3(self):
        return self.k * self.t * self.h * (self.m * self.V)

    def func4(self):
        if self.b <= self.V >= self.a:
            return 1
        elif self.V > self.a or self.V < self.b:
            return 0

    def func5(self):
        pass


if __name__ == '__main__':
    obj = BaseFunctions(3, 5, 2, 3, 4, 5, 6, 7)
    obj.counting_number_neurons()
    print obj.func1()
    print obj.func2()
    print obj.func3()
    print obj.func4()
    print obj.func5()
