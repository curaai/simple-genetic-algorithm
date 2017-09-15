import random
from gene import Gene

if __name__ == '__main__':
    length = 7
    case = 30
    target = 'a' * length
    parent = [' ' * length]

    for i in range(1000):
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
        excellence_score = [gene.score for gene in generation]
        average = round(sum(excellence_score) / len(excellence_score))
        excellence = [gene.chromosome for gene in generation if gene.score > average]
        try:
            parent = [random.choice(excellence) for x in range(4)]
        except IndexError:
            parent = [random.choice(generation) for x in range(4)]
            parent = [x.chromosome for x in parent]
        print(parent)
