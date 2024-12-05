import pandas as pd
import random

def generate_snps(num = 1):
    df = pd.DataFrame()

    df["SNP1"]= (random.choices([0,1,2], weights=[0.33,0.33,0.33], k=num))
    df["SNP2"]= (random.choices([0,1,2], weights=[0.20,0.20,0.60], k=num))
    df["SNP3"]= (random.choices([0,1,2], weights=[0.30,0.20,0.5], k=num))
    df["SNP4"]= (random.choices([0,1,2], weights=[0.7,0.2,0.1], k=num))
    df["SNP5"]= (random.choices([0,1,2], weights=[0.1,0.30,0.60], k=num))

    return df