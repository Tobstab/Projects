#using an adjacency list

edges = {1:[(1,0),(2,2),(6,9),(7,5)],2:[(1,2),(3,4),(7,6)],3:[(2,4),(8,5),(4,2)]}

u = 1
search = [1,2,3]
tree = [] #empty tree
cur_dist=0 
while search:
    cur = search.pop()
    tree.append(cur)
    #now search edges
    for edge, dist in edges[cur]:
        min_dist = min(min_dist, dist)

