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
        start = random.randint(0, int(len(self.parent)) - 1)
        end = random.randint(start, len(self.parent) - 1)
        self.chromosome = self.chromosome[:start] + self.parent[start:end] + self.parent[end:]

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
