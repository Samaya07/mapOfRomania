import numpy as np
class Graph:
    def __init__(self):
        self.edges={"Arad":["Zerind","Timisoara","Sibiu"],"Eforie":["Hirsova"],"Zerind":["Oradia","Arad"],
                    "Oradia":["Sibiu","Zerind"],"Mehadia":["Drobeta","Lugoj"],"Giurgiu":["Bucharest"],
                    "Timisoara":["Lugoj","Arad"],"Lugoj":["Mehadia","Timisoara"],"Drobeta":["Craiova","Mehadia"],
                    "Sibiu":["Fagaras","Rimnicu","Oradia","Arad"],"Craiova":["Rimnicu","Pitesti","Drobeta"],
                    "Rimnicu":["Craiova","Pitesti","Sibiu"],"Fagaras":["Bucharest","Sibiu"],
                    "Pitesti":["Bucharest","Rimnicu","Craiova"],"Bucharest":["Giurgiu","Urziceni","Pitesti","Fagaras"],
                    "Urziceni":["Hirsova","Vasluni","Bucharest"],"Hirsova":["Eforie","Urziceni"],"Neamt":["Iasi"],
                    "Vasluni":["Iasi","Urziceni"],"Iasi":["Neamt","Vasluni"],
                    }
        
        
        
        self.heuristic={"Arad":366,"Zerind":374,"Oradia":380,"Timisoara":329,"Lugoj":244,"Mehadia":241,"Hirsova":120,
                      "Drobeta":242,"Sibiu":253,"Craiova":160,"Rimnicu":193,"Pitesti":100,"Fagaras":176,
                      "Bucharest":0,"Giurgiu":77,"Urziceni":80,"Eforie":161,"Vasluni":199,"Iasi":226,"Neamt":234}
        
        
    def neighbors(self,node):
        return self.edges[node]
    
    def hsld(self,node):
        return self.heuristic[node]
    
def befs(graph,city,open,closed):
    for neighs in graph.neighbors(city):
        open.append([neighs,graph.hsld(neighs)])
    closed.append(city)
    open=sort_open(open)
    city=open[0][0]
    open.pop(0)
    if city==final:
        closed.append(final)
        return
    befs(graph,city,open,closed)
    
def sort_open(open):
    my_hsld=[]
    my_cities=[]
    for i in range(len(open)):
        my_hsld.append(open[i][1])
        my_cities.append(open[i][0])
    sorted_costs=np.argsort(my_hsld)
    open=[[my_cities[i],my_hsld[i]] for i in sorted_costs]
    return open
    
if __name__=='__main__':
    graph=Graph()
    open=[]
    closed=[]
    start='Arad'
    final='Bucharest'
    city=start
    befs(graph,city,open,closed)
    for city in closed:
        print(city,end='')
        if city!=final:
            print(' ---> ',end='')