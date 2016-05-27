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
                'set': set_of_chrom,
                'sum': amount
            }

            self.individuals.append(individual)

    def selection(self):
        """The calculation of a share of chromosomes"""
        self.get_total_amount()

        for item in self.individuals:
            item['percentage'] = self.get_percentage(item['sum'])

        random_values = [random.randint(1, 99) for _ in self.individuals]

        self.get_number_of_shares()
        self.number_of_shares.insert(0, 0)  # to correctly determine the range

        shares = self.get_share_of_individuals(random_values)

        # print(shares)
        pairs = self.get_pairs(shares)
        # print(pairs)

        self.crossing(pairs)

    def crossing(self, list_of_pairs):
        """Apply genetic operators of crossover and mutation"""
        for pair in list_of_pairs:
            print pair
            # TODO is whether the upper limit of the number of chromosomes
            Lk = random.randint(1, 7)
            first = self.individuals[pair[0] - 1]['set']
            second = self.individuals[pair[1] - 1]['set']

            # first individual
            first_set_value = first[:Lk] + second[Lk:]
            print first_set_value
            print 'Last sum {}, current sum {}'.format(
                self.individuals[pair[0] - 1]['sum'],
                sum(first_set_value))
            self.individuals[pair[0] - 1]['set'] = first_set_value
            self.individuals[pair[0] - 1]['sum'] = sum(first_set_value)

            # second individual
            second_set_value = second[:Lk] + first[Lk:]
            print second_set_value
            print 'Last sum {}, current sum {}'.format(
                self.individuals[pair[1] - 1]['sum'],
                sum(second_set_value))
            self.individuals[pair[1] - 1]['set'] = second_set_value
            self.individuals[pair[1] - 1]['sum'] = sum(second_set_value)
            print('-' * 20)

    # helper functions
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
                self.number_of_shares.append(
                    self.individuals[index]['percentage'])

    def get_share_of_individuals(self, random_values):
        """Obtaining the number of individual entries"""
        ch_i = []

        for i in random_values:
            for index, j in enumerate(self.number_of_shares):

                if index < len(self.number_of_shares):
                    if i > j and i < self.number_of_shares[index + 1]:
                        # print('{} < {} < {}'
                        #       .format(j, i, self.number_of_shares[index + 1]))
                        ch_i.append(self.number_of_shares.index(j) + 1)
                        break

        return ch_i

    def get_pairs(self, individuals):
        """
        Getting pairs for crossing

        -> [2, 2, 5, 4, 5, 4]
        <- [(2, 5), (2, 4), (5, 4)]
        """
        list_of_pairs = []
        while individuals:
            for first in individuals:
                for second in individuals:
                    if first != second:
                        list_of_pairs.append((
                            individuals.pop(individuals.index(first)),
                            individuals.pop(individuals.index(second))
                        ))
                        break
                break

        return list_of_pairs

if __name__ == '__main__':
    obj = Genetic(6, 10)
    obj.generate_individuals()
    pprint.pprint(obj.individuals)

    print '*' * 100
    obj.selection()
    pprint.pprint(obj.individuals)
