"""
Main code
"""
import polars as pl
#import numpy as np


# Download World Development Indicators
def development(data): 
    data = pl.read_csv("https://media.githubusercontent.com/media/nickeubank/MIDS_Data/master/World_Development_Indicators/wdi_small_tidy_2015.csv")
    return data.describe()
    #return data["Adolescent fertility rate (births per 1,000 women ages 15-19)"].describe().loc['mean']

# generate Plot

import seaborn.objects as so
from matplotlib import style

def plot(data):
    my_chart = (so.Plot(data, x="Mortality rate, infant (per 1,000 live births)", y="GDP per capita (constant 2010 US$)")
    .add(so.Line(), so.PolyFit(order=2))
    .add(so.Dot())
    .label(title="Log GDP and infat Mortality")
    .theme({**style.library["seaborn-whitegrid"]}))
    my_chart.show()
