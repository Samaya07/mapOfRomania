def bfs(map,city,open,closed,parent_dict):
    if city not in closed:
        closed.append(city)         #append the city to expand in the closed(explored) list
        for neighs in map[city]:
            if neighs not in parent_dict:
                parent_dict[neighs]=city  #storing the parent of the current city in parent_dict for future backtracking to find final path
            open.append(neighs)       #the children of the current node are added at the end of the open(frontier) list
        if final in open:
            return
        city=open[0]       #the first element in the open list is made the city to be next traversed
        open.pop(0)        #it is removed from the open

    else:
        city=open[0]     #if the current city is already in the closed list the next city
        open.pop(0)      #is made as the current city to avoid loops
    bfs(map,city,open,closed,parent_dict)
    

map={"Arad":["Sibiu","Zerind","Timisoara"],
     "Zerind": ["Arad","Oradia"],
     "Timisoara":["Arad","Lugoj"],
     "Oradia":["Zerind","Sibiu"],
     "Lugoj":["Timisoara","Mehadia"],
     "Sibiu":["Oradia","Arad","Rimnicu","Fagaras"],
     'Mehadia': ['Lugoj', 'Drobeta'],
    'Drobeta': ['Mehadia', 'Craiova'],
    'Craiova': ['Drobeta', 'Rimnicu', 'Pitesti'],
    'Rimnicu': ['Sibiu', 'Craiova', 'Pitesti'],
    'Fagaras': ['Sibiu', 'Bucharest'],
    'Pitesti': ['Rimnicu', 'Craiova', 'Bucharest'],
    'Bucharest': ['Fagaras', 'Pitesti','Giurgiu','Urziceni'],
     'Giurgiu' : ['Bucharest'],
     'Urziceni' : ['Bucharest','Hirsova','Vasluni'],
     'Hirsova': ['Urziceni','Eforie'],
     'Eforie' : ['Hirsova'],
     'Vasluni' : ['Urziceni','Iasi'],
     'Iasi' : ['Vasluni','Neamt'],
     'Neamt' : ['Iasi']}

print("Enter the initial location:")
initial=input()
print("Enter the destination:")
final=input()
city=initial
open=[]
closed=[]
parent_dict={}
path=[final]
bfs(map,city,open,closed,parent_dict)
path_city=closed[-1]
while(path_city!=initial):
    path.append(path_city)
    path_city=parent_dict[path_city]
path.append(initial)
answer=path[::-1]
for city in answer:
    print(city,end='')
    if city!=final:
        print(' ---> ',end='')
