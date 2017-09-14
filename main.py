import random
from gene import Gene

if __name__ == '__main__':
    length = 7
    case = 30
    target = 'a' * 5
    parent = [' ' * 5] * 2

    for i in range(20):
        # make generation
        generation = [Gene(random.choice(parent)) for x in range(case)]

        # get score each Gene
        for gene in generation:
            gene.fitting(target)

        # check
        for gene in generation:
            if gene.chromosome == target:
                print(gene.chromosome)
                print('success')
                exit(0)

        # select good parent
        result = []
        for gene in generation:
            [result.append(gene.chromosome) for i in range(gene.score)]

        parent = [random.choice(result) for x in range(2)]
        print(parent)

    print()
