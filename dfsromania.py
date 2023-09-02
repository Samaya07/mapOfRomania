def dfs(map,city,open,closed,parent_dict):
    if city not in closed:
        closed.append(city)   
        i=0
        for neighs in map[city]:
            if neighs not in parent_dict:
                parent_dict[neighs]=city
            open.insert(i,neighs)   #in dfs the children of current city are added at the start of the list
            i=i+1                   #unlike bfs where they are appended at the end.
        if final in open:
            return
        city=open[0]
        open.pop(0)
    else:
        city=open[0]
        open.pop(0)

    dfs(map,city,open,closed,parent_dict)


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
open=[]
closed=[]
print("Enter the initial location:")
initial=input()
print("Enter the destination:")
final=input()
city=initial
parent_dict={}
path=[final]

dfs(map,city,open,closed,parent_dict)

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