import turtle as tr
import canvasvg
import datetime
from pprint import pprint


class RenderingNeuralNetwork(object):
    def __init__(self):
        self.wn = tr.Screen()
        self.pen = tr.Turtle()
        self.pen.speed(0)
        self.pen.hideturtle()

    def draw_neuron(self, center, radius):
        """Rendering a single neuron"""
        self.pen.up()
        self.pen.goto(center)

        self.pen.setheading(0)
        self.pen.forward(radius)
        self.pen.setheading(90)
        self.pen.pendown()

        self.pen.circle(radius)
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
        self.radius = 20
        self.height = 640
        self.width = 1200
        self.central_coordinates = {}  # the coordinates of centers of neurons

    def distance_between_layers(self):
        return self.width / self.number_of_layers

    def distance_between_neurons(self):
        distance = self.height / self.number_of_neurons_in_layer
        if self.number_of_neurons_in_layer > 6:
            self.radius -= self.number_of_neurons_in_layer / 20.0
            return distance
        else:
            return distance - 50

    def calculate_center_coordinates(self):
        """
        The calculation of the centers of the neurons
        (the distance between neurons, the distance between layers)
        """
        coord_y = 0
        coord_x = 0
        distance_between_l = self.distance_between_layers()
        distance_between_n = self.distance_between_neurons()

        for index_l, layer in enumerate(xrange(1, self.number_of_layers + 1)):
            layer_data = []
            if index_l:
                coord_x += distance_between_l
            else:
                coord_x = -640  # starting coordinates X

            for index_n, neuron in enumerate(xrange(1, self.number_of_neurons_in_layer + 1)):

                if index_n:
                    coord_y -= distance_between_n
                else:
                    coord_y = 320  # starting coordinates Y

                layer_data.append((coord_x, coord_y))

            self.central_coordinates[layer] = layer_data

        pprint(self.central_coordinates)


if __name__ == '__main__':
    draw = RenderingNeuralNetwork()

    def darw_link(target, layer):
        for neuron in layer:
            draw.draw_link(target, neuron)

    calc = CalculationDistance(3, 2)
    calc.calculate_center_coordinates()
    for layer in sorted(calc.central_coordinates.keys()):
        for n in calc.central_coordinates[layer]:
            draw.draw_neuron(n, calc.radius)

    for index, layer in enumerate(sorted(calc.central_coordinates.keys()), 1):
        for n in calc.central_coordinates[layer]:
            if index != len(calc.central_coordinates.keys()):
                darw_link(n, calc.central_coordinates[layer + 1])

    # s = SaveImage()
    # s.save()
    tr.mainloop()

    # TODO: layers paint in different colors
    # Todo: add input and output parameters
