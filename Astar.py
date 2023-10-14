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
        
        self.weights={"AradZerind":75,"ZerindOradia":71,"AradTimisoara":118,"TimisoaraLugoj":111,"LugojMehadia":70,
                      "MehadiaDrobeta":75,"AradSibiu":140,"OradiaSibiu":151,"DrobetaCraiova":120,
                      "CraiovaRimnicu":146,"CraiovaPitesti":138,"SibiuFagaras":99,"SibiuRimnicu":80,
                      "RimnicuPitesti":97,"FagarasBucharest":211,"PitestiBucharest":101,"BucharestGiurgiu":90,
                      "BucharestUrziceni":85,"UrziceniHirsova":98,"HirsovaEforie":86,"UrziceniVasluni":142,
                      "VasluniIasi":92,"IasiNeamt":87}
        
        self.heuristic={"Arad":366,"Zerind":374,"Oradia":380,"Timisoara":329,"Lugoj":244,"Mehadia":241,"Hirsova":120,
                      "Drobeta":242,"Sibiu":253,"Craiova":160,"Rimnicu":193,"Pitesti":100,"Fagaras":176,
                     "Bucharest":0,"Giurgiu":77,"Urziceni":80,"Eforie":161,"Vasluni":199,"Iasi":226,"Neamt":234}
        
        #self.heuristic={"Iasi":210,"Neamt":180,"Vasluni":250,"Urziceni":260,"Hirsova":300,"Eforie":350,"Bucharest":200,
         #               "Giurgiu":260,"Pitesti":100,"Fagaras":0,"Rimnicu":90,"Craiova":200}
    def neighbors(self,node):
        return self.edges[node]
    
    def get_cost(self,from_node,to_node):
        if from_node==to_node:
            return 0
        else:
            list_weights=list(self.weights.keys())
            if (from_node+to_node) in list_weights:
                return self.weights[(from_node + to_node)]
            else:
                return self.weights[(to_node + from_node)]
    
    def hsld(self,node):
        return self.heuristic[node]
    
def sort_open(open):
    my_heur=[]
    my_cities=[]
    my_pathcost=[]
    for i in range(len(open)):
        my_heur.append(open[i][1])
        my_cities.append(open[i][0])
        my_pathcost.append(open[i][2])
    sorted_costs=np.argsort(my_heur)
    open=[[my_cities[i],my_heur[i],my_pathcost[i]] for i in sorted_costs]
    return open

    
def astar(graph,city,open,closed,path_cost,parent_list):
    for neighs in graph.neighbors(city):
        step_cost=graph.get_cost(city,neighs)
        fcost=graph.hsld(neighs)+path_cost+step_cost
        parent_list.append([[neighs,fcost],[city,path_cost+graph.hsld(city)]])
        open.append([neighs,fcost,path_cost+step_cost])
    closed.append(city)
    open=sort_open(open)
    city=open[0][0]  
    path_cost=open[0][2]
    open.pop(0)
    if city==final:
        closed.append(final)
        return path_cost
    path_cost=astar(graph,city,open,closed,path_cost,parent_list)
    return path_cost
    
if __name__=='__main__':
    graph=Graph()
    open=[]
    closed=[]
    start='Arad'
    final='Bucharest'
    city=start
    path_cost=0
    parent_list=[]
    path_cost=astar(graph,city,open,closed,path_cost,parent_list)
    path=[final]
    path_city=closed[-1]
    city_and_cost=[path_city,path_cost]
    while(path_city!=start):
        for ele in parent_list:
            if ele[0]==city_and_cost:
                path_city=ele[1][0]
                path.append(path_city)
                city_and_cost=ele[1]
    
    answer=path[::-1]
    for city in answer:
        print(city,end='')
        if city!=final:
            print(' ---> ',end='')