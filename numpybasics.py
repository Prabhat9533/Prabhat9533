# import numpy as np
   #matrix= np.array([[1, 2], [3, 4]])
   #tensor = np.array([[[1, 2], [3, 4]], [[5, 6], [7, 8]]])

   #print(matrix)

import pandas as pd

data = {
    "name": ["Ali", "Sara", "John", "marry", "sachin", "virat", "Tony"],
    "marks": [85,90,65,65,45,85,35]
}

df = pd.DataFrame(data)

print(df.describe())



