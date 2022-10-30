from FitnessFunc import fitness

class Course:
    
    def __init__(self, name,size, time, room, professor, prefered, listed) -> None:
        self.name = name
        self.size = size
        self.time = time
        self.room = room
        self.professor = professor
        self.fitness = 0.0
        self.prefered = prefered
        self.listed = listed
        
    def getFitness(self):
        return self.fitness
    
    def setFitness(self, fitness):
        self.fitness = fitness
        
    def print(self) -> None:
        print(f'{self.name}, {self.time}, {self.room.building}, {self.room.number}, seats taken: ({self.size}/{self.room.capacity}), {self.professor}')
        
    def getElements(self):
        return [self.time,self.room,self.professor]
    
    def toFile(self):
        return f'{self.name}, {self.time}, {self.room.building}, {self.room.number}, seats taken: ({self.size}/{self.room.capacity}), {self.professor}\n'
