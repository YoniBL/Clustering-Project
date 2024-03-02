import numpy as np
def print_matrix(matrix):
    for i in range(len(matrix)):
        for j in range(len(matrix[i]) - 1):
            print("%.4f" % matrix[i][j], end=",")
        print("%.4f" % matrix[i][-1])

def euclidean_distance(x1, x2):
    return np.sqrt(np.sum((x1 - x2) ** 2))

def calculate_distance_matrix(data):
    n = len(data)
    distance_matrix = np.zeros((n, n))
    for i in range(n):
        for j in range(i+1, n):
            distance_matrix[i][j] = euclidean_distance(data[i], data[j])
            distance_matrix[j][i] = distance_matrix[i][j]  # Since the distance matrix is symmetric
    return distance_matrix

def find_closest_clusters(distance_matrix):
    min_distance = np.inf
    closest_clusters = None
    n = distance_matrix.shape[0]
    for i in range(n):
        for j in range(i+1, n):
            if distance_matrix[i][j] < min_distance:
                min_distance = distance_matrix[i][j]
                closest_clusters = (i, j)
    return closest_clusters


### by default we are doing the hierarchy clustering until there is one cluster, and we are using a complete linkage method
### If we wanna go for c amount of clusters, and use single linkage we can give second paramater amount of clusters and complete = False

def agglomerative_clustering(data, c = 1, complete = True):
    tmp = data.copy()
    data = sorted(data, key = lambda x : sum(x)) ## sort data to get consistent clustering process for the same data in different order
    vector_size = len(data[0])
    data = np.array(data)
    clusters = [data[i] for i in range(len(data))]  # Initially, each data point is its own cluster
    distance_matrix = calculate_distance_matrix(data)

    while len(clusters) > c:
        i, j = find_closest_clusters(distance_matrix)
        new_cluster =np.concatenate((clusters[i], clusters[j]), axis=0)
        clusters.pop(j)
        clusters.pop(i)
        clusters.append(new_cluster)
        for k in range(len(clusters)):
            if k != i and k != j:
                if complete :
                  d = max(distance_matrix[i][k], distance_matrix[j][k])
                else :
                  d = min(distance_matrix[i][k], distance_matrix[j][k])
                distance_matrix[i][k] = d
                distance_matrix[k][i] = d
        distance_matrix = np.delete(distance_matrix, j, axis=0)
        distance_matrix = np.delete(distance_matrix, j, axis=1)
    clusters = list(clusters)
    for i in range(len(clusters)):
        clusters[i] = list(clusters[i])
    final_clusters = []
    for cluster in clusters :
        final_cluster = [cluster[i:i + vector_size] for i in range(0, len(cluster), vector_size)]
        final_clusters.append(final_cluster)

    return final_clusters


