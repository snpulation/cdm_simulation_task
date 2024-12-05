#Generate BP from height

hypertension_status = []

for height in generate_height:
    if height >= 170:
        bp = random.choices(population =["yes", "no"], weights = [0.2, 0.8])
        hypertension_status.append(bp[0])
    if height < 170:
        bp = random.choices(population = ["yes", "no"], weights = [0.1, 0.9])
        hypertension_status.append(bp[0])

print(hypertension_status)
          