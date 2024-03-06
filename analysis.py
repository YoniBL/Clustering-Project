import sys
import numpy as np

import agglomerative_clustering
import kmeans
import symnmf
from sklearn.metrics import silhouette_score

def import_points(data):
    all_vectors = []
    for line in data:
        vector = line.split(",")
        for i in range(len(vector)):
            vector[i] = float(vector[i])
        all_vectors.append(vector)
    return all_vectors

def H_centers(H):
    return [row.index(max(row)) for row in H]

def main():
    args_amount = len(sys.argv)
    if args_amount != 3:
        print("An Error Has Occurred")
        return

    file_in = sys.argv[2]
    file = open(file_in)
    all_vectors = import_points(file)
    str_k = sys.argv[1]
    if not str_k.isdigit():
        print("Invalid number of clusters!")
        return
    k = int(str_k)
    if k < 1:
        print("Invalid number of clusters!")
        return

    kmeans.init(k, all_vectors)
    kmeans.kMean(k, all_vectors)
    kmeans_labels = kmeans.get_Label(all_vectors)

    h = symnmf.final_H(all_vectors, len(all_vectors), len(all_vectors[0]), k)
    symnmf_labels = H_centers(h)

    aggo_clustering_clusters = agglomerative_clustering.agglomerative_clustering(all_vectors, k)
    data_points = [point for cluster in aggo_clustering_clusters for point in cluster]

    # Assign labels to data points based on cluster index
    agglo_labels = np.concatenate([np.full(len(cluster), i) for i, cluster in enumerate(aggo_clustering_clusters)])

    silhouette_kmeans = silhouette_score(all_vectors, kmeans_labels)
    silhouette_symnmf = silhouette_score(all_vectors, symnmf_labels)
    silhoutte_aggo = silhouette_score(data_points, agglo_labels )
    print(f"k means labels are : {kmeans_labels}")
    print(f"symnmf labels are : {symnmf_labels}")
    print("nmf:", silhouette_symnmf)
    print("kmeans:", silhouette_kmeans)
    print("hierercial :", silhoutte_aggo)


if __name__ == "__main__":
    main()
