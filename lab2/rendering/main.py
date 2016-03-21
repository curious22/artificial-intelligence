import turtle as tr
import canvasvg
import datetime


class RenderingNeuralNetwork(object):
    def __init__(self):
        self.wn = tr.Screen()
        self.pen = tr.Turtle()
        self.pen.speed(0)
        self.pen.hideturtle()
        self.central_coordinates = {}  # the coordinates of the centers of the neurons

    def draw_neuron(self, center):
        """Rendering a single neuron"""
        self.pen.up()
        self.pen.goto(center)

        self.pen.setheading(0)
        self.pen.forward(20)
        self.pen.setheading(90)
        self.pen.pendown()

        self.pen.circle(5)
        self.pen.up()
        self.pen.goto(center)
        self.pen.setheading(0)

    def draw_link(self, first_dot, second_dot):
        """Connecting neurons between them."""
        self.pen.up()
        self.pen.goto(first_dot)

        self.pen.down()
        self.pen.goto(second_dot)

    def calculation_distance(self):
        """Calculation of distance between neurons, layers."""
        pass


class SaveImage(object):
    def __init__(self):
        self.extension = '.svg'

    def save(self):
        canvas = tr._getscreen().getcanvas()
        canvasvg.saveall(self.generate_name() + self.extension, canvas)

    def generate_name(self):
        return datetime.datetime.now().strftime('%d-%m-%Y_%H:%M:%S')


class CalculationDistance(object):
    def __init__(self, number_of_layers, number_of_neurons_in_layer):
        self.number_of_layers = number_of_layers
        self.number_of_neurons_in_layer = number_of_neurons_in_layer


if __name__ == '__main__':
    draw = RenderingNeuralNetwork()
    data = {
        'l1': [
            (60, 40),
            (40, 40),
            (20, 40),
            (0, 40)
        ]
    }
    for layer in data:
        for n in data[layer]:
            draw.draw_neuron(n)
    s = SaveImage()
    s.save()
    tr.mainloop()
