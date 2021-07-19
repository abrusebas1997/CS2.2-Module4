import math

def get_min(visited, table, neighbors):
  #optional helper function to find next neighbor to look AttributeError
  pass

def build_shortest_path(graph, start):
  #return a shortest path table
  table = {}
  # take the form
  #{vertex: [cost, previous]}
  #{"Port Sarim": [0, ""],}

  # Get vertices

  #Initialize table
  #vertices
  #Initial costs, 0 and infinity, math.inf
  #precious, init as empty strings
  unvisited = []
  for v in graph.keys():
    unvisited.append(v)
    if v == start:
      table[v] = [0, ""]
    else:
      table[v] = [math.inf, ""]

  print(table)
  print(unvisited)

  current = start
  #look at a vertex (start with the given start)
  #look at its neighbors (for loop to look at all neighbors)


  while current != None:
      visited = []
      neighbors = graph[current]
      print("Current: ", current)
      print("Neighbors", neighbors)
      for n in neighbors:
        if n[0] not in visited:
          #update costs of neighbors in the table
          #take the current vertice's know cost from the table
          #add it to the cost of the neighbor from the graph
          neighbor_name = n[0]
          print("Neighbor", neighbor_name)
          neighbor_cost = n[1]
          current_cost = table[current][0]
          print("Neighbor cost", neighbor_cost)
          print("Current cost", current_cost)
          distance = current_cost + neighbor_cost
          print("Distance", distance)

          #update the table with cost ONLY if the distance is LESS than the recorded distance in the table for the neighbor
          cost_in_table = table[neighbor_name][0]
          if distance < cost_in_table:
            #update the table
            table[neighbor_name][0] = distance
            #update the previous vertex in the table
            table[neighbor_name][1] = current


  #once I'm done looking at all neighbors
      print(table)
      print(unvisited)
      unvisited.remove(current)
      if len(unvisited) != 0:
          current = unvisited[0]
      else:
          current = None


  # print("current")
  # print(current)
  #replace current vertex with the lowest cost neighbor
  #look at neighbors not in visited and pick the one with lowest cost in table to look at next
  #initial min = infinity
  #loop through neighbors
  #if neighbor not in visited
  #get the neighbor's current cost from the table
  #if the neighbor's current cost from the table
  #at end should have neighbor with lowest cost
  #update current to be that neighbor


  #keep doing this until all vertices are visited, some way of keeping track of what we've visited
  #while I len of visited < len of my total list of vertices

  return table

def get_shortest_path(table, start, end):
    list_of_places = []
    list_of_places.append(end)
    current = end
    while current != start:
        # table[current]
        # print(table[current][1])
        current = table[current][1]
        list_of_places.append(current)
        print(list_of_places)
    list_of_places.reverse()
    return list_of_places



  #return the shortest path given the table
  #start at the end and keep looking at previous vertices


example_graph = {"Port Sarim":[("Darkmeyer", 10), ("Al Kharid", 4)], "Darkmeyer":[("Port Sarim", 10), ("Al Kharid", 4), ("Varrock", 3), ("Nardah", 2)], "Al Kharid": [("Port Sarim", 4), ("Darkmeyer", 4), ("Varrock", 2)], "Varrock":[("Al Kharid", 2), ("Darkmeyer", 3), ("Nardah", 3)], "Nardah": [("Varrock", 3), ("Darkmeyer", 2)]}

table = build_shortest_path(example_graph, "Darkmeyer")

print(get_shortest_path(table, "Darkmeyer", "Nardah"))
