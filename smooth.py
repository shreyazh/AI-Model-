import pandas as pd
h = pd.read_csv('data.csv')
import matplotlib.pyplot as plt
h.hist(bins=50, figsize=(20,15))
