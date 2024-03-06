import numpy as np

epsilon = 0.001
centers = []
d = {}
default_iter = 200
muK = []


def init(k, all_vectors):
    for i in range(k):
        centers.append(all_vectors[i])
        d[i] = []
        muK.append(10)

def distance(vector1, vector2):
    sum = 0
    for i in range(len(vector1)):
        sum += (vector1[i]-vector2[i])**2
    return sum**0.5

def choose_center(vector):
    min = distance(vector, centers[0])
    index_chosen = 0
    for i in range(1, len(centers)):
        d = distance(vector, centers[i])
        if d<min:
            min = d
            index_chosen = i
    return index_chosen


def update_center(index):
    last_center = centers[index]
    vectors = d[index]
    vector_size = len(vectors[0])
    new_center = [0 for i in range(vector_size)]
    num_of_vectors = len(vectors)
    for i in range(vector_size):
        for vec in vectors:
            new_center[i] += vec[i]
        new_center[i] = new_center[i]/num_of_vectors
    centers[index] = new_center
    muK[index] = distance(last_center, new_center)

def update_all_centers(k):
    for i in range(k):
        update_center(i)

def kMean(K, all_vectors, iter=default_iter):
    for i in range(iter):
        counter = 0
        for i in range(K):
            d[i] = []
        for vector in all_vectors:
            d[choose_center(vector)].append(vector)
        update_all_centers(K)
        for mu in muK:
            if mu < epsilon:
                counter += 1
            else :
                break
        if counter == K:
            break

def get_Label(all_vectors) :
    label = []
    for vector in all_vectors :
        label.append(choose_center(vector))
    return label
