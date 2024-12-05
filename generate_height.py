from datetime import datetime
import pandas as pd
from scipy.stats import truncnorm

# set distribution parameters based on literature https://elifesciences.org/articles/20320
BIRTH_DECADES = [1940, 1950, 1960, 1970, 1980]
HEIGHT_DIST = pd.DataFrame(
    data = {
        "men_mean": [177.4, 178.4, 179.0, 179.9, 178.4],
        "men_sd": [6.73, 6.96, 7.49, 7.55, 7.59],
        "women_mean": [163.7, 164.4, 165.1, 165.9, 164.7],
        "women_sd": [6.19, 6.58, 7.00, 7.27, 7.07],
    }
)
HEIGHT_DIST.index = BIRTH_DECADES

# param processing 
GENDER_MAP = {
    1: "men", 
    0: "women"
}

# restrict to realistic values based on historical data
HEIGHT_LB = 54.6 # https://en.wikipedia.org/wiki/Chandra_Bahadur_Dangi
HEIGHT_UB = 272 # https://en.wikipedia.org/wiki/Robert_Wadlow

def generate_height(age, gender, num_samples=1):
    birth_decade = (datetime.now().year - age) // 10 * 10
    if birth_decade not in BIRTH_DECADES:
        birth_decade = max(BIRTH_DECADES) # use most recent estimates

    mean = HEIGHT_DIST.loc[birth_decade, GENDER_MAP[gender] + "_mean"]
    sd = HEIGHT_DIST.loc[birth_decade, GENDER_MAP[gender] + "_sd"]

    a = (HEIGHT_LB - mean) / sd
    b = (HEIGHT_UB - mean) / sd

    return truncnorm.rvs(a, b, loc=mean, scale=sd, size=num_samples, random_state=42)


if __name__ == "__main__":
    print(generate_height(80, 1, 10)) # sample heights for 80-yo men
    print(generate_height(18, 0, 10)) # sample heights for 18-yo women