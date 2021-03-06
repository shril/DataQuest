import pandas as pd
from sklearn.cluster import KMeans

votes = pd.read_csv('114_congress.csv')


kmeans_model = KMeans(n_clusters=2, random_state=1)

senator_distances= kmeans_model.fit_transform(votes.iloc[:,3:])

# extract the cluster labels
labels = kmeans_model.labels_
# print(labels)
# [1 1 0 1 0 0 1 0 1 0 0 1 0 1 0 0 0 1 1 1 1 0 1 1 1 1 1 1 0 0 1 1 0 1 1 0 1
#  0 1 1 1 0 1 1 0 1 1 1 1 0 0 1 0 1 0 1 1 0 1 0 1 0 0 0 1 1 0 0 0 1 1 0 1 0
#  1 1 1 1 1 0 1 0 0 1 1 0 1 0 1 0 1 1 1 0 1 0 0 0 1 0]

# make a table comparing these labels to votes["party"] with crosstab().
print(pd.crosstab(labels, votes["party"]))
# party   D  I   R
# row_0           
# 0      41  2   0
# 1       3  0  54

# The index is the cluster (row_0), in this case think of a cluster as senators who have similar voting patterns
# For each unique value in the party column the crosstab() method will print out a table comparing labels to votes["party"]