import random
import pprint


class Genetic(object):

    def __init__(self, number_of_individuals, number_of_chromosomes):
        self.number_of_individuals = number_of_individuals
        self.number_of_chromosomes = number_of_chromosomes
        self.individuals = []
        self.total_amount = 0
        self.number_of_shares = []

    def get_order_chromosome(self):
        """Generate the order of chromosome"""
        order = [random.choice([0, 1])
                 for _ in range(self.number_of_chromosomes)]
        return order

    def generate_individuals(self):
        """The generation of all animals individuals"""
        for i in range(self.number_of_individuals):
            set_of_chrom = self.get_order_chromosome()
            amount = sum(set_of_chrom)
            individual = {
                'number': i + 1,
                'set': set_of_chrom,
                'sum': amount
            }

            self.individuals.append(individual)

    def selection(self):
        """The calculation of a share of chromosomes"""
        self.get_total_amount()

        for item in self.individuals:
            item['percentage'] = self.get_percentage(item['sum'])

        random_values = [random.randint(0, 100) for _ in self.individuals]
        print(random_values)

        self.get_number_of_shares()

    def get_total_amount(self):
        for i in self.individuals:
            self.total_amount += i['sum']

    def get_percentage(self, sum_c):
        result = (float(sum_c) / self.total_amount) * 100
        return round(result, 3)

    def get_number_of_shares(self):
        """
        -> [4, 8, 67, 87, 50]
        <- [20.0, 43.333, 63.333, 80.0, 100.0]
        """
        for index, i in enumerate(self.individuals):
            if index != 0:
                value = (self.number_of_shares[index - 1] +
                         self.individuals[index]['percentage'])
                self.number_of_shares.append(round(value, 3))
            else:
                self.number_of_shares.append(self.individuals[index]['percentage'])

    def crossing(self):
        """Apply genetic operators of crossover and mutation"""
        pass

if __name__ == '__main__':
    obj = Genetic(5, 10)
    obj.generate_individuals()
    obj.selection()
    print(obj.number_of_shares)
    # pprint.pprint(obj.individuals)
