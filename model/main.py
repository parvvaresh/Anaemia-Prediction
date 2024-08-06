import pandas as pd
from classification import classification

df = pd.read_csv("./data/anaemia_dataset.csv")

classification(df, "Anaemic")