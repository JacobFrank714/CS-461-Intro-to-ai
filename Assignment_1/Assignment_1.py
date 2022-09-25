from queue import PriorityQueue
from math import sqrt

cities = {}
adj = {}

class City:
    # Object with the city's name, x coordinate, y coordinate, and if it has been checked
    def __init__(self, name,x,y):
        self.name = name
        self.x = float(x)
        self.y = float(y)
        self.visited = False
        

def best_first_search(actual_Src, target):
    # Queue for keeping track of what city are currently in scope for being checked
    pq = PriorityQueue()
    # puts first city in queue with cost 0 (cost, city Object) 
    pq.put((0, cities[actual_Src]))
    
    while pq.empty() == False:
        u = pq.get()[1]
        u.visited = True
        # Displaying the path having lowest cost
        print(u.name, end=", ")
        # Checks to see if the current City is the target
        if u.name == target:
            break
        # Adding each adjacent city to current city to the Queue
        for c in adj[u.name]:
            # c is a dict {"city name": float -> cost from current city}
            if cities[list(c.keys())[0]].visited == False:
                # If City isn't in Queue, add it else continue
                cities[list(c.keys())[0]].visited = True
                pq.put((list(c.values())[0], cities[list(c.keys())[0]])) 
                
    print("No Path")
    
def findCost(x1,x2,y1,y2):
    # Finds the cost from city 1 to city 2
    cost = sqrt((x2 - x1)**2 + (y2 - y1)**2)
    return cost

def mapCity():
    # Makes a list of cities with their coordinates
    with open("Assignment_1\coordinates.txt") as f:
        while True:
            coords = f.readline()
            if coords == '':
                break
            coords = coords.split()
            cities[coords[0]] = (City(coords[0], coords[1], coords[2]))
            adj[coords[0]]=[]
            
def adjacencies():
    # Makes a list of all adjacencies for each city and the cost from current city to each adjacent city
    with open("Assignment_1\Adjacencies.txt") as f:
        while True:
            # Read in each set of adjacencies
            line = f.readline()
            # Checks for EOF
            if line == "":
                break
            # Split each line into a list of city names
            line = line.split()
            # Iterates through each city in the adjacenty line
            for i in line:
                # Adds each city to the current i's adjacency list
                for j in line:
                    # Skips adding itself to the adjacencies
                    if j == i:
                        continue
                    # Supposed to skip duplicates
                    elif j in adj[i]:
                        continue
                    # Adds current City j to Adjacency list with it's cost from the city i
                    else:
                        adj[i].append({j:findCost(cities[i].x,cities[j].x,cities[i].y,cities[j].y)})

if __name__ == "__main__":
    mapCity()
    adjacencies()
    
    source = input("Starting City: ")
    target = input("Target City: ")
    
    best_first_search(source, target)