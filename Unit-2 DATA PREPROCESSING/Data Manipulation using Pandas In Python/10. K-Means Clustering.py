from sklearn.datasets import load_iris
from sklearn.cluster import KMeans
iris = load_iris()
model = KMeans(n_clusters=3, random_state=42)
model.fit(iris.data)
print("Cluster Labels:")
print(model.labels_)
