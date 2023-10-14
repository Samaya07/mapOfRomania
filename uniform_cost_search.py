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
    def neighbors(self,node):
        return self.edges[node]
    def get_cost(self,from_node,to_node):
        list_weights=list(self.weights.keys())
        if (from_node+to_node) in list_weights:
            return self.weights[(from_node + to_node)]
        else:
            return self.weights[(to_node + from_node)]

def ucs(graph,city,open,closed,parent_list,path_cost):
    if city not in closed:
        closed.append(city)
        for neighs in graph.neighbors(city):
            cost=graph.get_cost(city,neighs)+path_cost
            parent_list.append([[neighs,cost],[city,path_cost]])
            open.append([neighs,cost])
        open=sort_list(open)
        city=choose_first(open)
        path_cost=open[0][1]
        open=pop_first(open)
    else:
        city=choose_first(open)
        path_cost=open[0][1] 
        open=pop_first(open)
    if city==final:
        closed.append(final)
        return path_cost
    path_cost=ucs(graph,city,open,closed,parent_list,path_cost)
    return path_cost

def sort_list(open):
    my_costs=[]
    my_values=[]
    for i in range(len(open)):
        my_costs.append(open[i][1])
        my_values.append(open[i][0])
    sorted_costs=np.argsort(my_costs)
    open=[[my_values[i],my_costs[i]] for i in sorted_costs]
    return open

def choose_first(open):
    city=open[0][0] 
    return city

def pop_first(open):
    open.pop(0)
    return open

if __name__=='__main__':
    graph=Graph()
    start=input("Enter the start city:")
    final=input("Enter the destination city:")
    city=start
    open=[]
    closed=[]
    path_cost=0
    parent_list=[]
    path_cost=ucs(graph,city,open,closed,parent_list,path_cost)
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
    print("\nPath cost:",path_cost)           
