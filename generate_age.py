import numpy as np

def generate_age(num_samples = 1):
    # target population: adults age 18 to 80 
    # sample age from a uniform distribution from 18 to 80
    # assume perfectly representative data
    return np.random.uniform(low=18, high=80, size=num_samples)

if __name__ == "__main__":
    print(generate_age(10)) # test sample 10 values