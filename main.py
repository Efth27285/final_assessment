import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv('finance_liqour_sales.csv')

total_sales = sum(df['sale_dollars'])
sales = df.groupby(by=['store_name']).agg({'sale_dollars': 'sum'})
sorted_sales = sales.apply(lambda x: x.sort_values(ascending=True))
per_sorted_sales = sorted_sales.apply(lambda x: (x / total_sales) * 100).round(2).tail(15)
zip = df['zip_code']
bottles = df['bottles_sold']

p = plt.scatter(zip.index, bottles.values.flatten())
plt.title('%Sales by store')
plt.xlabel('%Zip Code', fontsize=12)
plt.ylabel('Bottles Sold', fontsize=1)
plt.xlim(right=15)
plt.xlim([0, 200])
plt.ylim([0, 2000])
plt.show()
