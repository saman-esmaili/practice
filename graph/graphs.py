import networkx as nx
from matplotlib import pyplot as plt
import numpy as np
class Generator():
    def generate(self):
        self.matrix = np.array([
            [0,0,0,0,1,1,0],
            [0,0,0,0,0,0,0],
            [0,0,0,1,0,0,0],
            [1,0,0,0,0,0,0],
            [0,1,0,0,0,0,0],
            [0,0,1,0,0,0,0],
            [1,1,0,0,0,0,0]
        ])
        graph = nx.from_numpy_array(self.matrix,create_using=nx.DiGraph)

        self.show_lables = {0:"A",1:"B",2:"C",3:"D",4:"E",5:"F",6:"G"}
        self.lables = {"A":0,"B":1,"C":2,"D":3,"E":4,"F":5,"G":6}
        graph = nx.relabel_nodes(graph,self.show_lables)

        nx.draw(graph,with_labels=True,node_color="lightblue",edge_color="gray",arrows=True)
        plt.show()

        return self.matrix,self.lables
