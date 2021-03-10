# Spectral-Clustering

The .py file contains a class that performs a spectral clustering. This is done by first computing the point cloud into a graph with an epsilon-ball, i.e. an edge is put whenever the distance between two points is less than epsilon. Afterwards the K (cluster components) eigenvectors associated to the K smallest eigenvalues are computed, and lastly on these elements it is performed a K-means algorithm that gives the final result. 
https://arxiv.org/pdf/0711.0189.pdf
