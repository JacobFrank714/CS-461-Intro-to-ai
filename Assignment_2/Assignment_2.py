from Course import Course
from Room import Room
from FitnessFunc import fitness
import random
import numpy as np

rooms = [Room(building="FH",number="216",capacity=30),
         Room(building="FH",number="310",capacity=108),
         Room(building="MNLC",number="325",capacity=450),
         Room(building="Haag",number="201",capacity=60),
         Room(building="Haag",number="301",capacity=75),
         Room(building="Royall",number="206",capacity=75),
         Room(building="Royall",number="201",capacity=50),
         Room(building="Katz",number="003",capacity=45),
         Room(building="Bloch",number="119",capacity=60)]
profs = ["Gharibi", "Gladbach", "Hare", "Nait-Abdesselam", "Shah", "Song", "Uddin", "Xu", "Zaman", "Zein el Din"]

solutions = []
for s in range(500):
    solutions.append((Course(name = "CS101A", size=50, time = random.randint(10,15), room = random.choice(rooms), professor = random.choice(profs), prefered=['Gladbach', 'Gharibi', 'Hare', 'Zein el Din'], listed=['Zaman', 'Nait-Abdesselam']),
                      Course(name = "CS101B", size=50, time = random.randint(10,15), room = random.choice(rooms), professor = random.choice(profs), prefered=['Gladbach', 'Gharibi', 'Hare', 'Zein el Din'], listed=['Zaman', 'Nait-Abdesselam']), 
                      Course(name = "CS191A", size=50, time = random.randint(10,15), room = random.choice(rooms), professor = random.choice(profs), prefered=['Gladbach', 'Gharibi', 'Hare', 'Zein el Din'], listed=['Zaman', 'Nait-Abdesselam']),
                      Course(name = "CS191B", size=50, time = random.randint(10,15), room = random.choice(rooms), professor = random.choice(profs), prefered=['Gladbach', 'Gharibi', 'Hare', 'Zein el Din'], listed=['Zaman', 'Nait-Abdesselam']),
                      Course(name = "CS201", size=50, time = random.randint(10,15), room = random.choice(rooms), professor = random.choice(profs), prefered=['Gladbach', 'Hare', 'Zein el Din', 'Shah'], listed=['Zaman', 'Nait-Abdesselam', 'Song']),
                      Course(name = "CS291", size=50, time = random.randint(10,15), room = random.choice(rooms), professor = random.choice(profs), prefered=['Gharibi', 'Hare', 'Zein el Din', 'Song'], listed=['Zaman', 'Nait-Abdesselam', 'Shah', 'Xu']),
                      Course(name = "CS303", size=60, time = random.randint(10,15), room = random.choice(rooms), professor = random.choice(profs), prefered=['Gladbach', 'Zein el Din', 'Hare'], listed=['Zaman', 'Song', 'Shah' ]),
                      Course(name = "CS304", size=25, time = random.randint(10,15), room = random.choice(rooms), professor = random.choice(profs), prefered=['Gladbach', 'Hare', 'Xu'], listed=['Zaman', 'Song', 'Shah',  'Nait-Abdesselam', 'Uddin', 'Zein el Din']),
                      Course(name = "CS394", size=20, time = random.randint(10,15), room = random.choice(rooms), professor = random.choice(profs), prefered=['Xu', 'Song'], listed=['Nait-Abdesselam', 'Zein el Din']),
                      Course(name = "CS449", size=60, time = random.randint(10,15), room = random.choice(rooms), professor = random.choice(profs), prefered=['Xu', 'Song', 'Shah' ], listed=['Zein el Din', 'Uddin' ]),
                      Course(name = "CS451", size=100, time = random.randint(10,15), room = random.choice(rooms), professor = random.choice(profs), prefered=['Xu', 'Song', 'Shah'], listed=['Zein el Din', 'Uddin',  'Nait-Abdesselam', 'Hare'])))
    
bestSolution={'fitness': -20}
averageFitScores = []
for i in range(200):
    
    rankedsoutions = []
    totalfit = 0.0
    for s in solutions:
        sol = dict(schedule = s, fitness = fitness(s))
        rankedsoutions.append(sol)
        totalfit += sol['fitness']
    for s in rankedsoutions:
        s['fitness'] = s['fitness'] / totalfit
    avgFit = totalfit / len(solutions)
    averageFitScores.append(avgFit)
        
    rankedsoutions = sorted(rankedsoutions, key=lambda x: x['fitness'], reverse=True)
    
    if rankedsoutions[0]['fitness'] > bestSolution['fitness']:
        bestSolution = rankedsoutions[0]
    
    print(f"=== Gen {i} best solutions ===")
    
    for i in range(11):
        rankedsoutions[0]['schedule'][i].print()
    print('Highest fit score:',rankedsoutions[0]['fitness'])
    print('Average fit for gen:',avgFit)
    print('Best fitness score ever:',bestSolution['fitness'])

    if i >= 100:
        if ((averageFitScores[i] - averageFitScores[i-100]) / 100) < 1:
            break
    
    bestsolutions = rankedsoutions[:100]
    
    elements = []
    for s in bestsolutions:
        elements.append(s['schedule'][0].getElements())
        elements.append(s['schedule'][1].getElements())
        elements.append(s['schedule'][2].getElements())
        elements.append(s['schedule'][3].getElements())
        elements.append(s['schedule'][4].getElements())
        elements.append(s['schedule'][5].getElements())
        elements.append(s['schedule'][6].getElements())
        elements.append(s['schedule'][7].getElements())
        elements.append(s['schedule'][8].getElements())
        elements.append(s['schedule'][9].getElements())
        elements.append(s['schedule'][10].getElements())
        
    newGen = []
    for _ in range(500):
            
        c1 = Course(name = "CS101A", size=50, time = random.choice(elements)[0], room = random.choice(elements)[1], professor = random.choice(elements)[2], prefered=['Gladbach', 'Gharibi', 'Hare', 'Zein el Din'], listed=['Zaman', 'Nait-Abdesselam'])
        
        c2 = Course(name = "CS101B", size=50, time = random.choice(elements)[0], room = random.choice(elements)[1], professor = random.choice(elements)[2], prefered=['Gladbach', 'Gharibi', 'Hare', 'Zein el Din'], listed=['Zaman', 'Nait-Abdesselam'])
        
        c3 = Course(name = "CS191A", size=50, time = random.choice(elements)[0], room = random.choice(elements)[1], professor = random.choice(elements)[2], prefered=['Gladbach', 'Gharibi', 'Hare', 'Zein el Din'], listed=['Zaman', 'Nait-Abdesselam'])
        
        c4 = Course(name = "CS191B", size=50, time = random.choice(elements)[0], room = random.choice(elements)[1], professor = random.choice(elements)[2], prefered=['Gladbach', 'Gharibi', 'Hare', 'Zein el Din'], listed=['Zaman', 'Nait-Abdesselam'])
        
        c5 = Course(name = "CS201", size=50, time = random.choice(elements)[0], room = random.choice(elements)[1], professor = random.choice(elements)[2], prefered=['Gladbach', 'Hare', 'Zein el Din', 'Shah'], listed=['Zaman', 'Nait-Abdesselam', 'Song'])
        
        c6 = Course(name = "CS291", size=50, time = random.choice(elements)[0], room = random.choice(elements)[1], professor = random.choice(elements)[2], prefered=['Gharibi', 'Hare', 'Zein el Din', 'Song'], listed=['Zaman', 'Nait-Abdesselam', 'Shah', 'Xu'])
        
        c7 = Course(name = "CS303", size=60, time = random.choice(elements)[0], room = random.choice(elements)[1], professor = random.choice(elements)[2], prefered=['Gladbach', 'Zein el Din', 'Hare'], listed=['Zaman', 'Song', 'Shah' ])
        
        c8 = Course(name = "CS304", size=25, time = random.choice(elements)[0], room = random.choice(elements)[1], professor = random.choice(elements)[2], prefered=['Gladbach', 'Hare', 'Xu'], listed=['Zaman', 'Song', 'Shah',  'Nait-Abdesselam', 'Uddin', 'Zein el Din'])
        
        c9 = Course(name = "CS394", size=20, time = random.choice(elements)[0], room = random.choice(elements)[1], professor = random.choice(elements)[2], prefered=['Xu', 'Song'], listed=['Nait-Abdesselam', 'Zein el Din'])
        
        c10 = Course(name = "CS449", size=60, time = random.choice(elements)[0], room = random.choice(elements)[1], professor = random.choice(elements)[2], prefered=['Xu', 'Song', 'Shah' ], listed=['Zein el Din', 'Uddin' ])
        
        c11 = Course(name = "CS451", size=100, time = random.choice(elements)[0], room = random.choice(elements)[1], professor = random.choice(elements)[2], prefered=['Xu', 'Song', 'Shah'], listed=['Zein el Din', 'Uddin',  'Nait-Abdesselam', 'Hare'])
        
        gen = (c1,c2,c3,c4,c5,c6,c7,c8,c9,c10,c11)
        if random.randrange(0, 1) <= 0.005:
            mutate = random.choice(gen)
            mutate.professor = random.choice(profs)
        if random.randrange(0, 1) <= 0.005:
            mutate = random.choice(gen)
            mutate.room = random.choice(rooms)
        if random.randrange(0, 1) <= 0.005:
            mutate = random.choice(gen)
            mutate.time = random.randint(10,15)
            
        newGen.append(gen)
        
    solutions = newGen
with open(file='./output.txt',mode='w') as f:
    f.write('Best Found Schedule:\n')
    for i in range(11):
        f.write(bestSolution['schedule'][i].toFile())