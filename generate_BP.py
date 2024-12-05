import random

#Generate BP from height
HEIGHT_THRESHOLD = 164

def generate_BP(height):
    if height >= HEIGHT_THRESHOLD:
        bp = random.choices(population =["yes", "no"], weights = [0.3, 0.7])
        return bp[0]
    if height < HEIGHT_THRESHOLD:
        bp = random.choices(population = ["yes", "no"], weights = [0.15, 0.85])
        return bp[0]

          