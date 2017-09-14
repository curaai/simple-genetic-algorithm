import random


class Gene:
    def __init__(self, parent, generation):
        self.list = "qwertyuiopasdfghjkklzxcvbnm"

        self.score = 0
        self.parent = parent
        self.chromosome = ' ' * len(parent)
        self.generation = generation

        self.legacy()
        self.generate()

    def legacy(self):
        n_legacy = random.randint(0, int(self.generation / 10))
        count = 0
        for i in range(len(self.chromosome)):
            if self.parent[i] == 'a':
                self.chromosome = self.chromosome[:i] + self.parent[i] + self.chromosome[i + 1:]
                count += 1
            if count == n_legacy:
                break

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
