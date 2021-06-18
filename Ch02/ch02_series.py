from numpy.core.records import array
import pandas as pd
import numpy as np


# numpy data
data = np.genfromtxt(
    'data/example_data.csv' , delimiter=';' , 
    names=True, dtype=None, encoding='UTF',
)

array_dict = {
    #this ia a list comprehension : https://www.w3schools.com/python/python_lists_comprehension.asp
    col: np.array([row[i] for row in data]) for i, col in enumerate(data.dtype.names)
}

# print (array_dict)

place = pd.Series(array_dict['place'], name='place')

#print(place)

place_index = place.index

#print(place_index)

df = pd.DataFrame(array_dict)

print(df)
print(df.values)
print(df.columns)