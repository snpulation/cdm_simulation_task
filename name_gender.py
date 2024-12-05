from faker import Faker
import numpy as np
import pandas as pd

fake =Faker()

def faker_categorical(num=1, seed=None):
    np.random.seed(seed)
    fake.seed_instance(seed)
    
    output = []
    for x in range(num):
      gender = np.random.choice(["1", "0"], p=[0.5, 0.5]) # male is 1, female is 0
      output.append(
        {
            "GivenName": fake.first_name_male() if gender=="1" else fake.first_name_female(),
            "Surname": fake.last_name(),
            "gender": gender,
            
        })
    return output

name_gender = pd.DataFrame(faker_categorical(num=500))
print(name_gender)

name_gender.to_csv('name_gender.csv',index = True, encoding= 'utf-8')