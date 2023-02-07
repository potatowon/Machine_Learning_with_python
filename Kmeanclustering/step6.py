from utils import get_dataset
from utils import get_initial_centroids
from utils import cal_which_cluster
from utils import clustering
from utils import update_centroids

dataset = get_dataset()
initial_centroid = get_initial_centroids(dataset, 4)
cluster = clustering(dataset, initial_centroid, 4)
update_centroid = update_centroids(cluster)