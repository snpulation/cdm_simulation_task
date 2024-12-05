import pandas as pd
from generate_BP import generate_BP
from generate_age import generate_age
from generate_countries import generate_country_city
from generate_education import generate_education
from generate_height import generate_height
from generate_bmi import generate_bmi
from generate_id import generate_id
from generate_snps import generate_snps
from name_gender import faker_categorical

NUM_SAMPLES = 500
df = pd.DataFrame(faker_categorical(num=NUM_SAMPLES))
ids = generate_id(num = NUM_SAMPLES)
df.insert(loc=0, column="ID", value=ids)
df["age"] = generate_age(num_samples = NUM_SAMPLES)
df["bmi"] = df.apply(lambda row: generate_bmi(row["gender"])[0], axis = 1)
df["height"] = df.apply(lambda row: generate_height(row["age"], row["gender"])[0], axis = 1)
countries, cities = generate_country_city(num_samples = NUM_SAMPLES)
df["country"] = countries
df["city"] = cities
df["education"] = generate_education(num = NUM_SAMPLES)

snps_df = generate_snps(num = NUM_SAMPLES)
df = pd.concat([df, snps_df], axis=1)

df["BP"] = df.apply(lambda row: generate_BP(row["height"]), axis = 1)


df.to_csv('final_simulated.csv', index = False, encoding= 'utf-8')