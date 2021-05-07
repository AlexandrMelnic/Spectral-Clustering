import numpy as np
import matplotlib.pyplot as plt
import networkx as nx


class Spectral_Clustering:
    
    def __init__(self, amplitude, epsilon):
        """Generates a data set composed by two concentric circles and then performes spectral
        clustering.

        Args:
            amplitude ([float]): list of two floats indicating the radiuses of the two circles.
            epsilon ([float]): the threshold parameter to put an arc between two similar nodes.
        """
        self.amplitude = amplitude
        self.epsilon = epsilon
        self.data = self.generate_data()
        self.edge_list = []
        self.create_edgelist()
        self.G = nx.Graph()
        self.create_graph()
        self.laplacian_eig()
        
    def y_coord(self, x, R):
        """Generates the y coordinate of the circle given the X and the radius.

        Args:
            x ([float]): X coordinates as an array/list.
            R ([type]): Radius of the circle.

        Returns:
            y ([float]): the y coordinate.
        """
        return np.sqrt(R**2-x**2)
    
    def generate_circle(self,amplitude):
        """Generates one circle with some given amplitude.

        Args:
            amplitude ([float]): Amplitude of the circle.

        Returns:
            [x,y] ([array float]): Returns the x,y coordinates of the circle.
        """
        x = np.random.random(500)*amplitude-amplitude/2
        y = self.y_coord(x,amplitude/2)
        x = np.concatenate((x, x))
        y = np.concatenate((y,-y))
        x = x + np.random.normal(0,0.1, size = len(x))
        y = y + np.random.normal(0,0.1, size = len(y))
        return np.array((x,y)).T
    
    def generate_data(self):
        """Genearates the matrix of data.

        Returns:
            [matrix of floats]: (,2) shape matrix containing the x and y coordinate.
        """
        return np.concatenate((self.generate_circle(self.amplitude[0]), 
                               self.generate_circle(self.amplitude[1])), axis = 0)
    
    def create_edgelist(self):
        """Generates the edge list from the data generated by the function generate_data.
        """
        for i in range(self.data.shape[0]):
            for node in np.where(np.sum((self.data[i]- self.data)**2, axis=1)<self.epsilon**2)[0]:
                if (i != node):
                    self.edge_list.append((i,node))
    
    def create_graph(self):
        """Addes the node the the graph G.
        """
        self.G.add_edges_from(self.edge_list)
    
    def laplacian_eig(self):
        """Computes the eigenvectors of the Laplacian of the graph.
        """
        L = nx.laplacian_matrix(self.G).todense()
        _, self.eig_vectors = np.linalg.eig(L)
        
    def cluster_plot(self):
        """Plots the graph with the clusters.
        """
        plt.figure(figsize=(10,10))
        cmap = [0 if x == 0 else 1 for x in self.eig_vectors[:,2]]
        nx.draw(self.G, pos = self.data, node_size = 30, node_color = cmap)
    

