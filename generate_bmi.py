from math import sqrt
from scipy.stats import truncnorm

# calculate simulation params using journal data from https://www.thelancet.com/pdfs/journals/lancet/PIIS0140-6736(16)30054-X.pdf
# CI = x  +/-  t*(s/√n)
# 24·2 kg/m² (24·0–24·4) in 2014 in 9·9 million men
men_mean = 24.2
men_sd = (24.4 - 24.0) / 3.92 * sqrt(9.9e6) # std err * sqrt n
# 24·4 kg/m² (24·2–24·6) in 2014 in 9·3 million women
women_mean = 24.4
women_sd = (24.6 - 24.2) / 3.92 * sqrt(9.3e6)

BMI_DIST = {
    # (mean, sd)
    1: (men_mean, men_sd), # male
    0: (women_mean, women_sd), # female
}

# restrict to realistic values based on historical data
BMI_LB = 6.7 # https://pubmed.ncbi.nlm.nih.gov/35569150/
BMI_UB = 251.1 # https://en.wikipedia.org/wiki/List_of_heaviest_people

# manually adjust variability of data
MAX_SD = 0.1

def generate_bmi(gender, num_samples=1):
    mean, sd = BMI_DIST[gender]
    # https://stackoverflow.com/questions/36894191/how-to-get-a-normal-distribution-within-a-range-in-numpy
    a = max((BMI_LB - mean) / sd, -1 * MAX_SD)
    b = min((BMI_UB - mean) / sd, MAX_SD)
    return truncnorm.rvs(a, b, loc=mean, scale=sd, size=num_samples, random_state=42)

if __name__ == "__main__":
    # print(BMI_DIST)
    print(generate_bmi(1, 10)) # test sample 10 men