import random
from gene import Gene

if __name__ == '__main__':
    length = 7
    case = 30
    target = 'a' * length
    parent = [' ' * length] * 2

    for i in range(100):
        # make generation
        generation = [Gene(random.choice(parent), i) for x in range(case)]

        # get score each Gene
        for gene in generation:
            gene.fitting(target)

        # check
        for gene in generation:
            if gene.chromosome == target:
                print([gene.chromosome for gene in generation])
                print(str(i) + 'generation success')
                exit(0)

        # select excellence parent
        excellence = []
        for gene in generation:
            [excellence.append(gene.chromosome) for i in range(gene.score)]
        parent = [random.choice(excellence) for x in range(4)]
        print(parent)
