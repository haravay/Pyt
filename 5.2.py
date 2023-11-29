import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

dataset = pd.read_csv('test.csv')
dataset_sample = dataset.head(1000)
missing_values = dataset_sample.isnull().sum()
print(missing_values)

plt.boxplot(dataset_sample['Square'].apply(np.log1p))
plt.xlabel('Square')
plt.ylabel('Значения (логарифмическая шкала)')
plt.title('Коробка с писюном')
plt.show()

plt.hist(dataset_sample['Square'], bins=10)
plt.xlabel('Square')
plt.ylabel('Частота')
plt.title('Гистограмма')
plt.show()

dataset_sample_filled = dataset.sample_fillna(0)

lower_bound = 0
upper_bound = 500
dataset_sample_processed = dataset_sample_filled[(dataset_sample_filled['Square'] > lower_bound) & (dataset_sample_filled['Square'] < upper_bound)]

room_counts = dataset_sample_processed['Rooms'].value_counts()
print(room_counts)

pivot_table = pd.pivot_table(dataset_sample_processed, values='Id', index='DistrictId', columns='Rooms', aggfunc='count')
print(pivot_table)

dataset_sample_processed.to_csv('surname.csv', index=False)
