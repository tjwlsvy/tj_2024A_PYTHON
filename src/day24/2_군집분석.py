# day24 > 2_군집분석.py

import pandas as pd
retail_df = pd.read_excel('Online Retail.xlsx')
print(retail_df.head())

retail_df = retail_df[retail_df['Quantity']>0]
retail_df = retail_df[retail_df['UnitPrice']>0]
retail_df = retail_df[retail_df['CustomerID'].notnull()]

retail_df['CustomerID'] = retail_df['CustomerID'].astype(int)
retail_df.info()
print(retail_df.isnull().sum())
print(retail_df.shape)

retail_df.drop_duplicates(inplace = True)
print(retail_df.shape)

pd.DataFrame([{
    'Product':len(retail_df['StockCode'].value_counts()), 'Transaction':len(retail_df['InvoiceNo'].value_counts()),
    'Customer':len(retail_df['CustomerID'].value_counts())}], columns=['Product' , 'Transaction' , 'Customer'], index=['counts'])

retail_df['Country'].value_counts()

retail_df['SaleAmount'] = retail_df['UnitPrice']*retail_df['Quantity']
print(retail_df.head())

aggregations = {
    'InvoiceNo' : 'count',
    'SaleAmount' : 'sum',
    'InvoiceDate' : 'max'
}

customer_df = retail_df.groupby('CustomerID').agg(aggregations)
customer_df = customer_df.reset_index()
# print(customer_df.head())

customer_df = customer_df.rename(columns= {'InvoiceNo' : 'Freq', 'InvoiceDate' : 'ElapsedDays'})
# print(customer_df.head())

import datetime

customer_df['ElapsedDays'] = datetime.datetime(2011,12,10)- customer_df['ElapsedDays']
print(customer_df.head())

customer_df['ElapsedDays'] = customer_df['ElapsedDays'].apply(lambda x : x.days+1)
print(customer_df.head())

import matplotlib.pyplot as plt
import seaborn as sns

fig, ax = plt.subplots()
ax.boxplot([customer_df['Freq'] , customer_df['SaleAmount'] , customer_df['ElapsedDays']],sym = 'bo')
plt.xticks([1,2,3] , ['Freq' , 'SaleAmount','ElapsedDays' ])
plt.show()

import numpy as np
customer_df['Freq_log'] = np.log1p(customer_df['Freq'])
customer_df['SaleAmount_log'] = np.log1p(customer_df['SaleAmount'])
customer_df['ElapsedDays_log'] = np.log1p(customer_df['ElapsedDays'])
print(customer_df.head())

fig , ax = plt.subplots()
ax.boxplot([customer_df['Freq_log'], customer_df['SaleAmount_log'], customer_df['ElapsedDays_log']], sym = 'bo')
plt.xticks([1,2,3,] , ['Freq_log' ,'SaleAmount_log' , 'ElapsedDays_log'])
plt.show()

from sklearn.cluster import KMeans
from sklearn.metrics import silhouette_score , silhouette_samples
x_features = customer_df[['Freq_log' , 'SaleAmount_log' , 'ElapsedDays_log']].values
from sklearn.preprocessing import StandardScaler
x_features_scaled = StandardScaler().fit_transform(x_features)

distortions = []

for i in range(1,11):
    kmeans_i = KMeans(n_clusters= i , random_state= 0 )
    kmeans_i.fit(x_features_scaled)
    distortions.append(kmeans_i.inertia_)

plt.plot(range(1,11) , distortions , marker = 'o')
plt.xlabel('Number of clusters')
plt.ylabel('Distortion')
plt.show()

kmeans = KMeans(n_clusters=3 , random_state=0)
y_labels = kmeans.fit_predict(x_features_scaled)
customer_df['ClusterLabel'] = y_labels
print(customer_df.head())


















