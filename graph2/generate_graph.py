import networkx as nx
from matplotlib import pyplot as plt
import numpy as np

class Graph():

    def generate(self):
        matrix = np.array([
            [0,0,0,0,0,1,0,0],
            [0,0,0,0,0,0,0,1],
            [1,1,0,1,0,0,0,0],
            [0,0,0,0,0,0,0,0],
            [0,0,0,0,0,0,1,0],
            [0,0,0,1,0,0,0,0],
            [0,0,0,0,0,0,0,1],
            [0,0,0,0,1,0,0,0]
        ])

        graph = nx.from_numpy_array(matrix,create_using=nx.DiGraph)

        lables = {"A":0,"B":1,"C":2,"D":3,"E":4,"F":5,"G":6,"H":7}
        show_lables = {0:"A",1:"B",2:"C",3:"D",4:"E",5:"F",6:"G",7:"H"}

        graph = nx.relabel_nodes(graph,show_lables)

        nx.draw(graph,with_labels=True,node_color="skyblue",edge_color="gray",arrows=True)
        plt.show()
        return lables,matrix
