aantalKluizenMax = 12
vrijeKluizen = []

def openFile(sort):
    return open('kluizen.txt', sort)


def closeFile(bestandnaam):
    bestandnaam.close()


def readFile():
    kluizentext = openFile('r')
    lines = kluizentext.readlines()
    closeFile(kluizentext)
    return lines


def writeFile(regel):
    kluizentext = openFile('a')
    kluizentext.write(regel)
    closeFile(kluizentext)
    return


def createFile():
    kluizentext = openFile('a')
    closeFile(kluizentext)


def printMenu():
    regel1 = 'Type het bijbehorende nummer om verder te gaan.'
    regel2 = '\n1: Ik wil weten hoeveel kluizen nog vrij zijn.'
    regel3 = '\n2: Ik wil een nieuwe kluis.'
    regel4 = '\n3: Ik wil even iets uit mijn kluis halen.'
    regel5 = '\n4: Ik geef mijn kluis terug.'
    print(regel1, regel2, regel3, regel4, regel5)


def vraagtOmInformatie():
    return str(input('Type hier u nummer: '))


def menuSelector():
    loop = 1
    while loop:
        nummer = vraagtOmInformatie()
        returntekst = ''
        if nummer == '1':
            returntekst = toonAantalKluizen()
            loop = 0
        elif nummer == '2':
            returntekst = nieuweKluis()
            loop = 0
        elif nummer == '3':
            returntekst = kluisOpenen()
            loop = 0
        elif nummer == '4':
            returntekst = kluisTerugvragen()
            loop = 0
        elif nummer == '5':
            returntekst = 'Deze functie werkt nog niet.'
            loop = 0
        else:
            print('U getal is geen menuoptie')
    return returntekst


def toonAantalKluizen():
    lstKluizen = aantalBeschikbareKluizen()
    regelMenuOptie1 = ('Er zijn ' + str(len(lstKluizen)) + ' kluizen vrij.')
    return regelMenuOptie1


def nieuweKluis():
    nieuwecode = ''
    meegeefStr = ''
    kluizenbeschikbaar = aantalBeschikbareKluizen()

    if len(kluizenbeschikbaar) > 0:
        print('Er zijn', len(kluizenbeschikbaar), 'kluizen beschikbaar, je krijgt kluis', kluizenbeschikbaar[0])
        code = wachtwoordCheck()
        nieuwecode = (str(vrijeKluizen[0]) + ';' + str(code))
        writeFile(nieuwecode)
        meegeefStr = 'Het is gelukt.'
    else:
        meegeefStr = 'Sorry, er is geen kluis beschikbaar.'

    return meegeefStr


def wachtwoordCheck():
    minWachtwoordLengte = 4
    wachtwoord = str(input('Geef alsjeblieft een code, moet bestaan uit min 4 characters: '))
    while len(wachtwoord) < minWachtwoordLengte:
        wachtwoord = str(input('Geef alsjeblieft een code, moet bestaan uit min 4 characters: '))
    wachtwoord += '\n'
    return wachtwoord


def kluisOpenen():
    regelMenuOptie3 = 'De kluis is open'
    line = kluisInfoVraag()
    lines = readFile()
    while line not in lines:
        print('deze combinatie bestaat niet')
        line = kluisInfoVraag()
    return regelMenuOptie3


def kluisTerugvragen():
    return 'deze functie is nog niet in gebruik'


def aantalBeschikbareKluizen():
    if len(vrijeKluizen) == 0:
        i = 1 #i is 1 want dit is het laagste kluisnummer
        while i < (aantalKluizenMax +1):
            vrijeKluizen.append(i)
            i += 1
    for line in readFile():
        nummer = line.split(';')[0]
        if nummer != '\n':
            nummer = int(nummer)
            if nummer in vrijeKluizen:
                vrijeKluizen.remove(nummer)
    return vrijeKluizen


def kluisInfoVraag():
    kluisnum = str(input('Geef je kluisnummer: '))
    kluiscode = str(input('Geef je wachtwoord: '))
    regel = (kluisnum + ';' + kluiscode + '\n')
    return regel


createFile()
printMenu()
grooteloop = 1
while grooteloop:
    print(menuSelector())
