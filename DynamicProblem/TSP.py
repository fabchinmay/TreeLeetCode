from itertools import permutations
from sys import maxsize
#https://www.youtube.com/watch?v=WIz6PppzYZE&ab_channel=SCALER
v=4

def TravellingSellsMan(graph,s):
    vertex=[]
    for i in range(v):
        if i!=s:
            vertex.append(i)

    minPath=maxsize
    next_Permutations = permutations(vertex)

    for i in next_Permutations:
        current_PathWeight= 0
        k=s

        for j in i:
            current_PathWeight +=graph[k][j]
            k=j
        current_PathWeight+=graph[k][s]
        minPath = min(minPath,current_PathWeight)


    return minPath

#graph = [[0,10,15,20],[10,0,35,25],[15,35,0,30],[20,25,30,0]]
graph = [[0,10,15,20],[5,0,9,10],[6,13,0,12],[8,8,9,0]]
s=0

print(TravellingSellsMan(graph,s))

