"""
ALGORITMO DE BÚSQUEDA BFS
Realizado por:
    - Carlos Montiel
    - Juan Sanchez
    - Esteban Alvarado
"""

from collections import deque

class TreeNode:
    
    def __init__(self, value, weight = 0):
        self.value = value
        self.weight = weight
        self.children = []
         
    def add_children(self, children):
        self.children.extend(children)
    
    def traverse(self, node):
        frontier = deque([node])
        while frontier:
            node = frontier.popleft()
            for child in node.children:
                frontier.append(child)
                print(child.value, child.weight)

n1 = TreeNode('Ellensburg')
n2 = TreeNode('Pendleton', 168)
n3 = TreeNode('Spokane', 175)
n4 = TreeNode('Spokane', 200)
n5 = TreeNode('Missoula', 356)
n6 = TreeNode('Pendleton', 200)
n7 = TreeNode('Missoula', 199)
n8 = TreeNode('BonnersFerry', 112)
n9 = TreeNode('Missoula', 249)
n10 = TreeNode('West Glacier', 176)
n11 = TreeNode('Missoula', 151)
n12 = TreeNode('Helena', 243)
n13 = TreeNode('GreatFalls', 211)
n14 = TreeNode('Havre', 231)
n15 = TreeNode('Butte', 119)
n16 = TreeNode('Helena', 111)
n17 = TreeNode('Helena', 65)
n18 = TreeNode('GreatFalls', 91)
n19 = TreeNode('Havre', 115)

n1.add_children([n2, n3])
n2.add_children([n4, n5])
n3.add_children([n6, n7, n8])
n8.add_children([n9, n10])
n10.add_children([n11, n12, n13, n14])
n11.add_children([n15, n16])
n15.add_children([n17])
n16.add_children([n18])
n18.add_children([n19])

##print("###BFS traverse###")
##n1.traverse(n1)
##print('#############\n')

#Nuevo commit
city_graph_dict={
    "Ellensburg":{"Pendleton":(168,1),"Spokane":(175,1)},
    "Pendleton":{"Spokane":(200,0),"Missoula":(356,0)},
    "Spokane":{"Pendleton":(200,0),"Missoula":(199,0),"Bonners_Ferry":(112,1)},
    "Bonners_Ferry":{"Missoula":(249,0),"West_Glacier":(176,1)},
    "West_Glacier":{"Missoula":(151,1),"Helena":(243,0),"Great_Falls":(211,0),"Havre":(231,0)},
    "Missoula":{"Butte":(119,1),"Helena":(111,1)},
    "Butte":{"Helena":(65,0)},
    "Helena":{"Great_Falls":(91,1)},
    "Great_Falls":{"Havre":(115,0)}
}

queue=["Ellensburg"]
parents=["Ellensburg"]
def bfs():
        print("1:",queue)
        current= queue.pop(0)
        parents.append(current)
        counter=0
        for son_key in city_graph_dict[current]:
            if not son_key in queue:
                queue.append(son_key)
                print("2:",queue)
                parents.append()
        parents.pop()
        for son_key in city_graph_dict[current]:
            if city_graph_dict[parents[len(parents)-1]][son_key][1]==1:
                bfs()
            else:
                queue.pop(0)





def bfs3():
    #Codigo implementado cercanamente segun Pseudocodigo del lubro
    node="Ellensburg"
    finalNode="Havre"
    #Se usa una double ended queue para simular comprotamiento de priority Queue
    frontier=deque()
    frontier.append(node)
    visited={node:0}
    while not frontier.__sizeof__()==0:
        if node==finalNode:
            return node,visited.get(node)
        node = frontier.popleft()
        nodeCost=visited.get(node)
        print("Padre",node,"Costo de recorrido:",nodeCost)
        for child in city_graph_dict.get(node):
            #Funcion EXPAND dentro de algoritmo:
            branch=child
            #Funcion para calcular el costo total que se ha hecho
            childrenCost=nodeCost+city_graph_dict.get(node).get(branch)[0]
            print("Hijo :", child,"Costo de recorrido: ",childrenCost)
            if not visited.__contains__(branch) or childrenCost<visited.get(branch):
                visited[branch]=childrenCost
                #Condicion para anadir al hijo en frontera en caso de que exista
                isBranch = city_graph_dict.get(node).get(branch)[1]
                if(isBranch==1):
                    frontier.append(branch)


bfs3()