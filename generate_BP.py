import random

#Generate BP from height

def generate_BP(height):
    if height >= 170:
        bp = random.choices(population =["yes", "no"], weights = [0.2, 0.8])
        return bp[0]
    if height < 170:
        bp = random.choices(population = ["yes", "no"], weights = [0.1, 0.9])
        return bp[0]

          