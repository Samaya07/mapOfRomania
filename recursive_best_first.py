class Graph:
    def __init__(self,initial,goal):
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
        self.initial_state=initial
        self.goal=goal
        
        #self.heuristic={"Iasi":210,"Neamt":180,"Vasluni":250,"Urziceni":260,"Hirsova":300,"Eforie":350,"Bucharest":200,
         #               "Giurgiu":260,"Pitesti":100,"Fagaras":0,"Rimnicu":90,"Craiova":200}
    def actions(self,node):
        return self.edges[node]
        
    def goal_test(self,node):
        if node==self.goal:
            return True
        
    def get_cost(self,from_node,to_node):
        if from_node==to_node:
            return 0
        else:
            list_weights=list(self.weights.keys())
            if (from_node+to_node) in list_weights:
                return self.weights[(from_node + to_node)]
            else:
                return self.weights[(to_node + from_node)]
    
    def heuristicc(self,node):
        return self.heuristic[node]
class Child_node:
    def __init__(self,problem,node,child):
        self.state=child
        self.g=problem.get_cost(node.state,child)
        self.h=problem.heuristicc(child)
        self.f=self.g+self.h
class Node:
    def __init__(self, state, g, h):
        self.state = state  # Current state
        self.g = g  # Path cost from the initial state to this state
        self.h = h  # Heuristic estimate of cost from this state to a goal

def recursive_best_first_search(problem):
    # Initialize RBFS with initial node and an infinite f-cost limit
    initial_node = Node(state=problem.initial_state, g=0, h=problem.heuristicc(problem.initial_state))
    path=[]
    result, path = rbfs(problem, initial_node, float('inf'),path)
    return result,path

def rbfs(problem, node, f_limit,path):
    if problem.goal_test(node.state):
        return node, path  # Solution found
    path.append(node)
    successors = []
    for action in problem.actions(node.state):
        child_node = Child_node(problem, node, action)
        successors.append(child_node)

    if not successors:
        return None, float('inf')  # Failure, return infinity

    while True:
        successors.sort(key=lambda x: x.f)  # Sort by f-value

        best = successors[0]
        if best.f > f_limit:
            return None, best.f  # Failure, return the best's f-value

        alternative = successors[1].f if len(successors) > 1 else float('inf')

        result, best.f = rbfs(problem, best, min(f_limit, alternative),path)
        if result is not None:
            return result, best.f

if __name__=='__main__':
    initial=input("Enter the initial state:")
    problem=Graph(initial,'Bucharest')
    print("The path from Arad to Bucharest using the Recursive Best first search is :\n")
    result,path=recursive_best_first_search(problem)
    for ele in path:
        print(ele.state,end='-->')
    print(result.state)
