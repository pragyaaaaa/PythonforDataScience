# Analysing the trend of top 10 basketball players over 10 years
import numpy as np
from DataSets import BasketballDataSet as d

print(d.Points)
mydata = np.arange(0, 20)
print(mydata)
print(np.reshape(mydata, (5, 4), order='C'))  # C for C-Programming language
print(np.reshape(mydata, (5, 4), order='F'))  # F for Fortran
