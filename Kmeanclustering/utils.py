import numpy as np
import matplotlib.pyplot as plt

def get_dataset():
    n_cluster_samples = 100
    means = [[1, 1], [-1, 1], [-1, -1], [1, -1]]
    stds = [0.5, 0.4, 0.3, 0.2]

    n_clusters = len(means)
    data = []
    for cluster_idx in range(n_clusters):
        cluster_data = np.random.normal(loc=means[cluster_idx],
                                        scale=stds[cluster_idx],
                                        size=(n_cluster_samples, 2))
        data.append(cluster_data)
    dataset = np.vstack(data)
    return dataset


def get_initial_centroids(dataset, K):
    datashuffle = dataset
    np.random.shuffle(datashuffle)
    X = datashuffle[:, 0][:K]
    Y = datashuffle[:, 1][:K]
    centroids = np.hstack([X.reshape(K, -1),Y.reshape(K, -1)])
    return centroids



def cal_which_cluster(dataset, centroids, sample_idx):
    pred = [[] for _ in range(len(centroids))]
    distance = np.sum((dataset[sample_idx] - centroids) ** 2, axis=1)
    # dist_argsort = np.argsort(distance)
    # pred[dist_argsort[0]].append(data_stack[idx].tolist())
    return distance

def clustering(dataset, centroids, K):

    clusters = [[] for _ in range(K)]
    for sample_idx in range(len(dataset)):
        distance = cal_which_cluster(dataset, centroids, sample_idx)
        dist_argsort = np.argsort(distance)
        clusters[dist_argsort[0]].append(dataset[sample_idx].tolist())
    return clusters

def update_centroids(clusters):
    update_centroid = []
    for idx in range(len(clusters)):
        avg = (np.sum(clusters[idx], axis=0)) / len(clusters[idx])
        update_centroid.append(avg)
    return update_centroid


