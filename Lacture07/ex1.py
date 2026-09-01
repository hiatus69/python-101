heroes = ['Ironman', 'Thor','Hulk','Spiderman']

def main():
    print(heroes)
    heroes.append('Antman')
    print("1",heroes)
    heroes.insert(1,'The Thing')
    print("2",heroes)
    heroes.remove('Thor')
    print("3",heroes)
    heroes.sort()   
    print("4",heroes)
    heroes.reverse()
    print("5",heroes)


main()