import math
### A* search algorith
### Created 02-12-17

def shortest_path(M,start,goal):
    print("shortest path called")
    
    # Nodes are tuples with id, parent, total cost, cost to goal + cost so far
    node = (start,None,0,distance(M,start,goal))
    
    # Initialize frontier to have start node and explored to be empty, both sets
    frontier = set()
    frontier.add(node)
    explored = set()
    exp_or_front = set()
    exp_or_front.add(node[0])
    
    # Assert that frontier is not empty (i.e. start node is given) and loop through frontier.    
    assert frontier != [], "No nodes found!"
    while(frontier != []):
        # Sort frontier by cost f (i.e. g + h, or cost to goal + cost so far) and expand lowest f node into explored
        lowest = sorted(frontier,key=lambda elem: elem[3])[0]
        frontier.remove(lowest)
        explored.add(lowest)
        exp_or_front.add(lowest[0])
        
        # If expanded node is goal, calculate route and return it.
        if(lowest[0] == goal):
            shortest = []
            curr = lowest
            while(curr[1] is not None): # Until we reach start node
                shortest.append(curr[0])
                curr = curr[1]
            shortest.append(start) # Loop ends before appending start node
            shortest.reverse() # path is in reverse
            return shortest
        for i in nearest_nodes(M,lowest[0]): # Loop through neighbors
            if(i in exp_or_front):           # Skip nodes that have already been seen
                continue
            curr_cost = lowest[2]+distance(M,lowest[0],i)
            node = (i,lowest,curr_cost,curr_cost+distance(M,i,goal))
            frontier.add(node)
            exp_or_front.add(node[0])
    assert frontier !=[], "No route found!"
        
def nearest_nodes(M,node):
    return M.roads[node]

def distance(M,node1, node2):
    x1, y1 = M.intersections[node1]
    x2, y2 = M.intersections[node2]
    return math.sqrt(pow(x1 - x2,2) + pow(y1 - y2,2))

