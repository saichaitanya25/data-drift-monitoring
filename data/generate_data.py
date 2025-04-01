import pandas as pd
import numpy as np

ref = pd.DataFrame({
    'feature1': np.random.normal(50, 10, 1000),
    'feature2': np.random.uniform(20, 80, 1000)
})
ref.to_csv('data/reference.csv', index=False)

new = pd.DataFrame({
    'feature1': np.random.normal(70, 15, 1000),
    'feature2': np.random.uniform(20, 80, 1000)
})
new.to_csv('data/new_data.csv', index=False)

print("Sample datasets created under /data")
