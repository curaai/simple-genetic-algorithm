import random


class Gene:
    def __init__(self, parent):
        self.list = "abcdef"

        self.score = 0
        self.parent = parent
        self.chromosome = ' ' * len(parent)

        self.legacy()
        self.generate()

    def legacy(self):
        n_legacy = random.randint(0, 2)
        for i in range(n_legacy):
            n = random.randint(0, len(self.parent) - 1)
            self.chromosome = self.chromosome[:n] + self.parent[n] + self.chromosome[n+1:]

    def generate(self):
        temp = ""
        for ch in self.chromosome:
            if ch is ' ':
                temp += random.choice(self.list)
            else:
                temp += ch
        self.chromosome = temp

    def fitting(self, target):
        score = 0
        for i in range(len(target)):
            if target[i] == self.chromosome[i]:
                score += 1
        self.score = score
