import numpy as np
from sklearn.cluster import KMeans
import matplotlib.pyplot as plt
 
# 假设我们有一些二维数据点
X = np.array([[1, 2], [1, 4], [1, 0], [4, 2], [4, 4], [4, 0]])
 
# 设定K值为2，即希望将数据划分为2个簇
kmeans = KMeans(n_clusters=2, random_state=0)
 
# 对数据进行拟合
kmeans.fit(X)
 
# 获取聚类标签和簇中心
labels = kmeans.labels_
centroids = kmeans.cluster_centers_
 
# 打印结果
print("Cluster labels:", labels)
print("Cluster centroids:\n", centroids)
 
# 可视化结果
plt.scatter(X[:, 0], X[:, 1], c=labels, cmap='viridis')
plt.scatter(centroids[:, 0], centroids[:, 1], c='red', s=300, alpha=0.5)
plt.title('K-means Clustering')
plt.xlabel('Feature 1')
plt.ylabel('Feature 2')
plt.show()
