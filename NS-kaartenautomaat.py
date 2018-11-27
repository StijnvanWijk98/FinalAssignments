stations = ['Schagen', 'Heerhugowaard', 'Alkmaar', 'Castricum', 'Zaandam', 'Amsterdam Sloterdijk',
            'Amsterdam Centraal', 'Amsterdam Amstel', 'Utrecht Centraal', "’s-Hertogenbosch", 'Eindhoven',
            'Weert', 'Roermond', 'Sittard', 'Maastricht']
eenstation = 5

def inlezenBeginstation(lst):
    loop = 1
    while loop:
        beginStation = str(input('Geef je beginstation: '))
        if beginStation in lst:
            print(beginStation)
            return beginStation


def inlezenEindStation(lst, beginstation):
    indexBeginStation = lst.index(beginstation)
    loop = 1
    while loop:
        eindStation = str(input('Geef je eindstation: '))
        if eindStation in lst:
            indexEindStation = lst.index(eindStation)
            if indexEindStation < indexBeginStation:
                print('De trein komt niet in', eindStation)
            else:
                print(eindStation)
                return eindStation
        else:
            print('De trein komt niet in', eindStation)


def omroepenReis(lst, beginstation, eindstation):
    indexBeginStation = (lst.index(beginstation)+1)
    indexEindStation = (lst.index(eindstation)+1)
    afstand = indexEindStation - indexBeginStation
    prijs = eenstation * afstand
    print('Het beginstation', beginstation, 'is het', (str(indexBeginStation) + 'e'), 'in het traject.')
    print('Het eindstation', eindstation, 'is het', (str(indexEindStation) + 'e'), 'in het traject.')
    print('De afstand bedraagt', afstand, 'station(s).')
    print('De prijs van deze rit is', prijs, 'euro.')

begin = inlezenBeginstation(stations)
eind = inlezenEindStation(stations, begin)
omroepenReis(stations, begin, eind)