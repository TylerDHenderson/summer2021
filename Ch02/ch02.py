import numpy as np


# numpy data
data = np.genfromtxt(
    'data/example_data.csv' , delimiter=';' , 
    names=True, dtype=None, encoding='UTF',
)

#print (data)
#print(f"the shape of the data: {data.shape}")
print(f"the data type of the data: {data.dtype}")

for row in data:
    print(f"Place: {row}")