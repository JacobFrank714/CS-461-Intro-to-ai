from queue import PriorityQueue
from math import sqrt

cities = {}
adj = {}

def best_first_search(actual_Src, target):
    pq = PriorityQueue()
    pq.put((0, cities[actual_Src]))
     
    while pq.empty() == False:
        u = pq.get()[1]
        # Displaying the path having lowest cost
        u.visited = True
        print(u.name, end=", ")
        if u.name == target:
            break
        
        for c in adj[u.name]:            
            if cities[list(c.keys())[0]].visited== False:
                cities[list(c.keys())[0]].visited = True
                pq.put((list(c.values())[0], cities[list(c.keys())[0]]))
                
    print()
    
def findCost(x1,x2,y1,y2):
    cost = sqrt((x2 - x1)**2 + (y2 - y1)**2)
    return cost

class City:
    
    def __init__(self, name,x,y):
        self.name = name
        self.x = float(x)
        self.y = float(y)
        self.visited = False
        
def mapCity():
    with open("Assignment_1\coordinates.txt") as f:
        while True:
            coords = f.readline()
            if coords == '':
                break
            coords = coords.split()
            cities[coords[0]] = (City(coords[0], coords[1], coords[2]))
            adj[coords[0]]=[]
            
def adjacencies():
    with open("Assignment_1\Adjacencies.txt") as f:
        while True:
            line = f.readline()
            if line == "":
                break
            line = line.split()
            for i in line:
                for j in line:
                    if j == i:
                        continue
                    elif j in adj[i]:
                        continue
                    else:
                        adj[i].append({j:findCost(cities[i].x,cities[j].x,cities[i].y,cities[j].y)})

if __name__ == "__main__":
    mapCity()
    adjacencies()
    
    source = input("Starting City: ")
    target = input("Target City: ")
    
    best_first_search(source, target)