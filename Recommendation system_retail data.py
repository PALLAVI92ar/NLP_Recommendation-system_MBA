# Importing libraries
import pandas as pd

# Importing dataset
df = pd.read_csv("retail_data2.csv")

# Preview data
pd.set_option('display.max_columns', None)
df.head()

# Dataset dimensions - (rows, columns)
df.shape

df.columns = ['0','1','2','3','4','5','6']

items  = df['0'].unique()

encodeddata = []
for index, row in df.iterrows():
    labels = {}
    uncommon = list(set(items)-set(row))
    common = list(set(items).intersection(row))
    for un in uncommon:
        labels[un] = 0
    for co in common:
        labels[co] = 1
    encodeddata.append(labels)

print(encodeddata)

encodeddata[0]
encodeddata[1]
encodeddata[2]
encodeddata[313]

############################
Edata  = pd.DataFrame(encodeddata)
Edata.shape
Edata.head()
############################

from mlxtend.frequent_patterns import apriori
freq_items = apriori(Edata,min_support=0.2,use_colnames=True)
freq_items
freq_items.tail()

from mlxtend.frequent_patterns import association_rules
rules = association_rules(freq_items, metric = 'confidence',min_threshold=0.2)
rules.to_csv("rules.csv")













