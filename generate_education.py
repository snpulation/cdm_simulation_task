import random

## primary - 18.2%
## high school - 30.12%
## bachelors - 45.18
## master - 4.5%
## phd - 2%
def generate_education(num = 1): 
    education_option=["Primary","High School","Bachelors","Masters","PHD"]
    education_weight=[18.2, 30.12, 45.18, 4.5, 2]
    return random.choices(education_option, weights=education_weight, k=num)
