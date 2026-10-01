heroes = ['ironman','Thor','Hulk','Superman','Spiderman']
h2 = ['Dr. Strange','Cpt, America','Black Panther','Ant man']

heroes.insert(0, h2[0])
print("0",heroes.index('Thor'))
heroes.insert(heroes.index('Thor'), h2[1])
print("1",heroes)
heroes.remove('Superman')
heroes.append('Ant Man')
print("2",heroes)
heroes.sort()
print("3",heroes)
heroes.reverse()
print("4",heroes)
newheroes = heroes 
newheroes[0] = 'Wonder Women'
print("5",heroes)
copyheroes = [] + heroes
print("6",copyheroes)
copyheroes[0] = 'Hanuman'
print("7",heroes)
print("8",copyheroes)