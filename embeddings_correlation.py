import numpy as np
from sklearn.metrics.pairwise import euclidean_distances
import scipy
from scipy import stats
from scipy.spatial import distance

def pc(low_dim_array, high_dim_array):
    # Calculate low dimension distance matrix
    # Pairwise distances
    low_dim_pairdist = euclidean_distances(low_dim_array, low_dim_array)
    high_dim_pairdist = euclidean_distances(high_dim_array, high_dim_array)


    # The pairwise matrix is symmetric, retain only the upper half
    upper_low_dim_pairdist = np.triu(low_dim_pairdist)
    upper_high_dim_pairdist = np.triu(high_dim_pairdist)


    # Prepare the array for the Person correlation: flattening
    upper_low_dim_pairdist_flat = upper_low_dim_pairdist.flatten()
    upper_high_dim_pairdist_flat = upper_high_dim_pairdist.flatten()

    #Calculate the Pearson correlation between the distances of data points in low and high embeddings
    p_corr, _ = scipy.stats.pearsonr(upper_low_dim_pairdist_flat, upper_high_dim_pairdist_flat)

    return p_corr, _, upper_low_dim_pairdist_flat, upper_high_dim_pairdist_flat
