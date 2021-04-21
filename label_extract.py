import numpy as np
from numpy import *
from pylab import *
import pandas as pd

def load_labels():
    Labels = genfromtxt('data/true_labels.csv',skip_header=0)
    print(Labels.shape)
    print(Labels[:10])
    print(type(Labels))

load_labels()
