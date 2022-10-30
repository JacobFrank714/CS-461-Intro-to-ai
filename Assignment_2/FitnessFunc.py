import numpy as np

def fitness(solution) -> float:
    score = 0.0

    for s in solution:
        courseScore = 0.0
        profClassCount = 1
        if s.room.capacity < s.size:
            courseScore -= 0.5
        elif s.room.capacity > (s.size * 3):
            courseScore -=0.2
        elif s.room.capacity > (s.size * 6):
            courseScore -= 0.4
        else:
            courseScore += 0.3
        if s.professor in s.prefered:
            courseScore += 0.5
        elif s.professor in s.listed:
            courseScore += 0.2
        else:
            courseScore -= 0.1
        for x in solution:
            if s.name == x.name:
                continue
            if s.time == x.time:
                if s.room == x.room:
                    courseScore -= 0.5
                if s.professor == x.professor:
                    courseScore -= 0.2                
                    profClassCount += 1
            if s.professor == x.professor:
                if abs(s.time - x.time) == 1:
                    if (s.room.building == "Bloch" and x.room.building == "Katz") or (s.room.building == "Katz" and x.room.building == "bloch"):
                        courseScore -= 0.4                   
            if s.name == 'CS101A' or s.name=='CS101B':
                if x.name == 'CS101B' or x.name == 'CS101A':
                    if (s.time == x.time) or (s.time ==(x.time - 1)) or (s.time == (x.time + 1)):
                        courseScore -= 0.5
                    if (abs(s.time - x.time)) >= 4:
                        courseScore += 0.5
                if x.name == 'CS191A' or x.name == 'CS191B':
                    if (s.time == (x.time + 1)) or (s.time == (x.time - 1)):
                        courseScore += 0.5                        
                        if (s.room.building == "Bloch" and x.room.building == "Katz") or (s.room.building == "Katz" and x.room.building == "bloch"):
                            courseScore -= 0.4
                    if (s.time == (x.time + 2)) or (s.time == (x.time - 2)):
                        courseScore += 0.25
                    if (s.time == x.time):
                        courseScore -= 0.25
            if s.name == 'CS191A' or s.name == 'CS191B':
                if x.name == 'CS191A' or x.name == 'CS191B':
                    if (s.time == x.time) or (s.time ==(x.time - 1)) or (s.time == (x.time + 1)):
                        courseScore -= 0.5
                    if (abs(s.time - x.time)) >= 4:
                        courseScore += 0.5
                if x.name == 'CS101B' or x.name == 'CS101A':
                    if (s.time == (x.time + 1)) or (s.time == (x.time - 1)):
                        courseScore += 0.5
                        if (s.room.building == "Bloch" and x.room.building == "Katz") or (s.room.building == "Katz" and x.room.building == "bloch"):
                            courseScore -= 0.4
                    if (s.time == (x.time + 2)) or (s.time == (x.time - 2)):
                        courseScore += 0.25
                    if (s.time == x.time):
                        courseScore -= 0.25
        if profClassCount > 4:
            courseScore -= 0.5
        elif profClassCount == 1 or profClassCount == 2:
            if s.professor == 'Xu':
                pass
            else:
                courseScore -= 0.4
        s.fitness = courseScore
        score += s.fitness
    
    return np.exp(score)